import requests
from fastapi import FastAPI, HTTPException, status

app = FastAPI()

API_KEY = "54fbc4d5deaed4f4bb00aba306e7dc06"


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/location/{city_name}")
async def location(city_name):
    geofinder_req = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={API_KEY}"
    )

    citylatlon = geofinder_req.json()

    print(citylatlon)

    if citylatlon == [] or citylatlon is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"city name: {city_name} not found.",
        )

    lat = citylatlon[0]["lat"]
    lon = citylatlon[0]["lon"]

    response = requests.get(
        url=f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )
    
    data = response.json()
    
    
    res = {
        "city": city_name,
        "lat": lat,
        "lon": lon,
        "temperature": data["main"]["temp"],
        "weather": data["weather"][0]["description"],
    }
    
    return data
