# GAME ANALYSER
Gaming data analyser


## Local Setup

git clone https://github.com/Sparsh216/Game-analyser.git

### Prerequisites 
1 -> Postgres installed and running at port 5432.
2 -> Docker installed and running.


## Using Docker
1 -> open docker file and setup these env vairables
ENV API_KEY = my-api-key
ENV DB_USERNAME = postgres
ENV DB_PASSWORD = 1234
ENV DB_HOST = localhost
ENV DB_PORT = 5432
ENV DATABASE = game_db

2-> run the below two commands

docker build -t fastapi-app .
docker run -d -p 8080:8080 fastapi-app

Your application is up and running at 8000.
Test it by navigating to http://localhost:8080.

## Using Terminal

1-> Create Virtual Environment
2-> Activate the Virtual Environment
3-> Create a .env file and setup these environment variables

ENV API_KEY = my-api-key
ENV DB_USERNAME = postgres
ENV DB_PASSWORD = 1234
ENV DB_HOST = localhost
ENV DB_PORT = 5432
ENV DATABASE = game_db

4-> Now Run Below commands

pip3 install -r requirements.txt
python3 main.py

Server is up and running at http://localhost:8080

5 -> Now to run the UI, Run below command

streamlit run streamlit_app.py

Streamlit is up at http://localhost:8501

## Remote Setup

1-> spin up an ec2 instance
2-> git pull the repo
3-> create virtual env and install requirements.txt
4-> using tmux run python3 main.py
5-> server is up and running in ip of that instance.

## CURL's To the deployed Soluntion


## Upload Curl

### Sample Request

curl --location 'https://game-analyser.onrender.com/upload_csv' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: my-api-key' \
--data '{
  "csvUrl": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSCtraqtnsdYd4FgEfqKsHMR2kiwqX1H9uewvAbuqBmOMSZqTAkSEXwPxWK_8uYQap5omtMrUF1UJAY/pub?gid=1439814054&single=true&output=csv"
}'

### Sample Response

{
    "message": "Data uploaded successfully"
}

## Querry Curl

### Sample Request

curl --location 'https://game-analyser.onrender.com/explore' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--header 'x-api-key: my-api-key' \
--data '{
  "filters": {"AppID":20200}
}'

Point to remember 
filters is where we need to querry our data

{
  "filters": {"Querry Field":Value}
}

make sure Querry Fields matches exactly the field name provided in csv "Case Senstive"

### Sample Response

{
    "count": 1,
    "data": [
        {
            "Release_date": "Oct 21, 2008",
            "Required_age": 0,
            "Price": 19.99,
            "Positive": 6,
            "Genres": "Casual,Indie,Sports",
            "AppID": 20200,
            "DLC_count": 0,
            "Tags": "Indie,Casual,Sports,Bowling",
            "About_the_game": "Galactic Bowling is an exaggerated and stylized bowling game with an intergalactic twist. Players will engage in fast-paced single and multi-player competition while being submerged in a unique new universe filled with over-the-top humor, wild characters, unique levels, and addictive game play. The title is aimed at players of all ages and skill sets. Through accessible and intuitive controls and game-play, Galactic Bowling allows you to jump right into the action. A single-player campaign and online play allow you to work your way up the ranks of the Galactic Bowling League! Whether you have hours to play or only a few minutes, Galactic Bowling is a fast paced and entertaining experience that will leave you wanting more! Full Single-player story campaign including 11 Characters and Environments. 2 Single-player play modes including Regular and Battle Modes. Head to Head Online Multiplayer play Modes. Super Powers, Special Balls, and Whammies. Unlockable Characters, Environments, and Minigames. Unlock all 30 Steam Achievements!",
            "Negative": 11,
            "Supported_languages": "['English']",
            "Score_rank": null,
            "Windows": true,
            "Developers": "Perpetual FX Creative",
            "Mac": false,
            "Publishers": "Perpetual FX Creative",
            "Categories": "Single-player,Multi-player,Steam Achievements,Partial Controller Support",
            "Name": "Galactic Bowling",
            "Linux": false
        }
    ]
}



## Hosted Querry UI

Provides less than and greater than filter as well

https://game-analyser-ui.onrender.com/

Enter filter field name and value and select less than or greater than if you want specifics
ans table will appear in the right hand side.


## Deployment cost on AWS 

EC2 Instance	$8.10  t2.micro 
Database (RDS)	~$13.00 db.t3.micro
Storage (S3)	~$0.01
Egress Data	~$0.03
Domain + SSL (opt)	~$1.50
Total	~$22–25/month