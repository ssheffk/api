from typing import Optional, Dict, List
import json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello we are in test environment"}


@app.get("/breakdowns", response_model=List[Dict])
async def get_damages():
    try:
        # Read the scraped data from the JSON file
        with open('daily_scraped_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        return {"error": "No data available"}

@app.get("/breakdowns/cities", response_model=Dict[str, object])
async def get_cities_with_damages():
    try:
        # Read the scraped data from the JSON file
        with open('daily_scraped_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Filter cities with non-empty damages and calculate the total damages
        cities_with_damages = [city["city"] for city in data if city.get("damages")]
        total_damages = sum(len(city["damages"]) for city in data if city.get("damages"))

        return {"cities": cities_with_damages, "total_damages": total_damages}


    except FileNotFoundError:
        return {"error": "No data available"}