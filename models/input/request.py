'''
Vendor request models
'''
from typing import Optional, Dict, Any

from pydantic import BaseModel


class UploadRequest(BaseModel):
    '''
    Upload request model
    '''
    csvUrl: Optional[str]

class QuerryRequest(BaseModel):
    '''
    Querry request model
    '''
    filters: Dict[str, Any]
