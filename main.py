import uvicorn

from fastapi import FastAPI, Request
from fastapi.security import HTTPBasic
from fastapi.responses import JSONResponse

from datetime import datetime
import urllib.request
import csv
from io import StringIO
from utils.logger import logger
from utils.db_utils import put_in_postgres
from configs.app import App
from configs.system import System

from models.input.request import UploadRequest, QuerryRequest
from models.dataModel.db_model import Game, initialize_database, get_session
from sqlalchemy.inspection import inspect
from sqlalchemy import String, Date, DateTime
from controllers.authentication.user import authenticated_user

app = FastAPI(title=App.NAME, version=App.VERSION)
security = HTTPBasic()


# Call on application startup
initialize_database()

@app.get("/health")
async def health_check() -> JSONResponse:
    '''
    Health check handler
    '''
    return JSONResponse(
        content={'message': 'server is up and running'},
        status_code=200
    )

@app.post("/upload_csv")
async def upload_csv(request: Request, payload:UploadRequest) -> JSONResponse:
    '''
    API for uploading csv
    '''
    # auth = authenticated_user(request=request)
    # if auth is False:
    #     return JSONResponse(
    #         content={
    #             'message': 'invalid x-api-key',
    #             'data': {}
    #         },
    #         status_code=403
    #     )

    try:
        response = urllib.request.urlopen(payload.csvUrl)
        csv_data = response.read().decode('utf-8')

        # Parse CSV data
        csv_reader = csv.DictReader(StringIO(csv_data))
        db = get_session()

        put_in_postgres(csv_reader=csv_reader, db=db)
        # Commit changes
        db.commit()
        db.close()

        return JSONResponse(
            content={'message': "Data uploaded successfully"},
            status_code=200
        )

    except urllib.error.HTTPError as e:
        return JSONResponse(
            content={'message':f"HTTP error: {e.reason}"},
            status_code=e.code
            )
    except Exception as e:
        return JSONResponse(
                    content={'message': "Server error occurred while fetching the CSV",
                             'error':f"{e}"},
                    status_code=500
                )



@app.post("/explore")
async def explore_data(request: Request, payload:QuerryRequest) -> JSONResponse:
    '''
    Explore API
    '''
    # auth = authenticated_user(request=request)

    # if auth is False:
    #     return JSONResponse(
    #         content={
    #             'message': 'invalid x-api-key',
    #             'data': {}
    #         },
    #         status_code=403
    #     )

    try:
        db = get_session()
        query = db.query(Game)

        # Get a list of all valid fields in the Game table
        valid_fields = {column.name for column in inspect(Game).columns}

        if not payload.filters:  # If filters are empty, return all data
            results = query.all()
            return {
                "count": len(results),
                "data": [result.__dict__ for result in results]
            }

        # Validate request filters
        for field in payload.filters.keys():
        # Check if the field is valid
            if not any(field.startswith(valid_field) for valid_field in valid_fields):
                return JSONResponse(
                    status_code=400,
                    content={'message': f"Invalid filter: '{field}' is not a valid field in the Game table."}
                )

        for field, value in payload.filters.items():
            if value is None:
                continue

            # Handle field operations like __gt and __lt
            if field.endswith("__gt") or field.endswith("__lt"):
                operation = "__gt" if field.endswith("__gt") else "__lt"
                base_field = field.split(operation)[0]

                # Check if the base field is valid
                field_obj = getattr(Game, base_field, None)
                if not field_obj:
                    return JSONResponse(
                        status_code=400,
                        content={'message': f"Invalid filter: '{base_field}' is not a valid field in the Game table."}
                    )

                if not isinstance(value, (int, float, str)):
                    return JSONResponse(
                        status_code=400,
                        content={
                            'message': f"Invalid filter: '{base_field}' requires a numeric or date value for '{operation}'."
                        }
                    )

                if operation == "__gt":
                    query = query.filter(getattr(Game, base_field) > value)
                else:
                    query = query.filter(getattr(Game, base_field) < value)

            else:
                # Exact match or LIKE operation
                field_obj = getattr(Game, field, None)
                if not field_obj:
                    return JSONResponse(
                        status_code=400,
                        content={'message': f"Invalid filter: '{field}' is not a valid field in the Game table."}
                    )

                field_type = field_obj.property.columns[0].type

                if isinstance(field_type, String):
                    # Handle string fields (LIKE operation)
                    if isinstance(value, str):
                        query = query.filter(field_obj.like(f"%{value}%"))
                    else:
                        return JSONResponse(
                            status_code=400,
                            content={
                                'message': f"Invalid filter: '{field}' requires a string value."
                            }
                        )
                elif isinstance(field_type, (Date, DateTime)):
                    # Handle exact date or datetime matching
                    if isinstance(value, (datetime.date, datetime.datetime)):
                        query = query.filter(field_obj == value)
                    else:
                        return JSONResponse(
                            status_code=400,
                            content={
                                'message': f"Invalid filter: '{field}' requires a valid date or datetime value."
                            }
                        )
                else:
                    # Default equality matching for other types
                    query = query.filter(field_obj == value)

            results = query.all()

            return {
                "count": len(results),
                "data": [result.__dict__ for result in results]
            }
        
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={
                'message': f"Error querying data: {e}"
            }
        )


api_v1 = FastAPI()


app.mount('/api/v1', api_v1)

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=System.Server.HOST, reload=App.DEBUG, port=System.Server.PORT,
        workers=1 # Workers default to 1 if debug is on
    )
