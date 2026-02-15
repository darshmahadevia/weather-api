# Weather API

A FastAPI-based weather API that fetches real-time weather data for any city using the OpenWeatherMap API.

## Features

- Get current weather information by city name
- Returns temperature, weather conditions, and geographic coordinates
- Built with FastAPI for high performance and automatic API documentation
- RESTful API endpoints

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd weather-api
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the development server:
```bash
fastapi dev app/main.py
```

2. The API will be available at `http://localhost:8000`

3. Access the interactive API documentation at `http://localhost:8000/docs`

## API Endpoints

### Root
```
GET /
```
Returns a welcome message.

**Response:**
```json
{
  "message": "hello world"
}
```

### Get Weather by City
```
GET /location/{city_name}
```
Fetches current weather data for the specified city.

**Parameters:**
- `city_name` (path parameter): Name of the city

**Example Request:**
```bash
curl http://localhost:8000/location/London
```

**Example Response:**
```json
{
  "coord": {
    "lon": -0.1257,
    "lat": 51.5085
  },
  "weather": [
    {
      "id": 801,
      "main": "Clouds",
      "description": "few clouds",
      "icon": "02d"
    }
  ],
  "main": {
    "temp": 15.5,
    "feels_like": 14.8,
    "temp_min": 14.2,
    "temp_max": 16.7,
    "pressure": 1013,
    "humidity": 72
  }
}
```

**Error Response:**
- `404 Not Found`: City not found
```json
{
  "detail": "city name: InvalidCity not found."
}
```

## Project Structure

```
weather-api/
├── app/
│   ├── __init__.py
│   └── main.py          # FastAPI application and endpoints
├── city.json            # City data (if applicable)
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Technologies Used

- **FastAPI**: Modern web framework for building APIs
- **OpenWeatherMap API**: Weather data provider
- **Uvicorn**: ASGI server for running the application
- **Requests**: HTTP library for API calls

## Requirements

- Python 3.7+
- Valid OpenWeatherMap API key (already configured in the code)

## Configuration

The API key is currently hardcoded in [app/main.py](app/main.py). For production use, consider using environment variables:

```python
import os
API_KEY = os.getenv("OPENWEATHER_API_KEY")
```

## Development

To run in development mode with auto-reload:
```bash
fastapi dev app/main.py
```

To run in production mode:
```bash
fastapi run app/main.py
```

## License

This project is part of the Roadmap.sh mini-projects series.

## Notes

- Temperature is returned in Celsius (metric units)
- The API uses OpenWeatherMap's geocoding API to convert city names to coordinates
- Rate limits apply based on your OpenWeatherMap API plan
