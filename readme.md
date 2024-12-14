curl --location 'https://game-analyser.onrender.com/upload_csv' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "csvUrl": "https://docs.google.com/spreadsheets/d/e/2PACX-1vSCtraqtnsdYd4FgEfqKsHMR2kiwqX1H9uewvAbuqBmOMSZqTAkSEXwPxWK_8uYQap5omtMrUF1UJAY/pub?gid=1439814054&single=true&output=csv"
}'

{
    "message": "Data uploaded successfully"
}



curl --location 'https://game-analyser.onrender.com/explore' \
--header 'accept: application/json' \
--header 'Content-Type: application/json' \
--data '{
  "filters": {"AppID":20200}
}'

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