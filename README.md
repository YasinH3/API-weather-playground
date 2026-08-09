# Weather API

A simple Python project that demonstrates how to fetch current weather data from public APIs.

## Overview

This repository contains two small example scripts:

- `main.py` uses the Open-Meteo geocoding and forecast APIs. It asks for a city name and prints the current temperature. It is open, without an API key needed.
- `OpenWeather.py` uses the OpenWeatherMap API to fetch weather details for a fixed city. And it displays more data. It is necessary an API key to run. 

## Requirements

- Python 3.12 or newer
- The `requests` package

## Installation

It is recommended to use a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
pip install requests
```

## Usage

To run a script (main.py or OpenWeather.py) there are two ways:
Either the city is an argument:
``` bash
python main.py CityName
python OpenWeather.py CityName
```
or is promted:
``` bash
python main.py 
python OpenWeather.py
```

## Project Structure

```text
Weather-API/
├── main.py
├── OpenWeather.py
├── pyproject.toml
└── README.md
```

## Notes

- The OpenWeatherMap script includes an API key in the file. Replace it with your own valid key if you want to use that example.
- This project is intended for learning how to work with REST APIs in Python.
