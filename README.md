# Weather API

A simple Python project for fetching current weather information for a city using public APIs.

## Overview

This repository includes two small example scripts:

- `main.py` - uses the Open-Meteo geocoding and forecast APIs to ask for a city name and print the current temperature.
- `OpenWeather.py` - uses the OpenWeatherMap API to fetch weather data for a fixed city.

## Requirements

- Python 3.12 or newer
- The `requests` package

Install the dependency with:

```bash
pip install requests
```

## Usage

Run the main script:

```bash
python main.py
```

When prompted, enter a city name such as `London` or `Madrid`.

## Project Structure

```text
Weather-API/
├── main.py
├── OpenWeather.py
├── pyproject.toml
└── README.md
```

## Notes

- The OpenWeatherMap example contains an API key in the script. Replace it with your own key if you want to use that script.
- This project is intended for learning how to work with REST APIs in Python.
