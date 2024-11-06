from typing import Optional, Dict, List
import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app = FastAPI()

# Allow your Svelte app origin
origins = [
    "http://localhost:5173",  # Replace with your local dev URL or production URL
    "https://avariite.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

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