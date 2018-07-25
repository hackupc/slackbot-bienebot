# HackUPC Slack bot

## Overview
HackUPC Slack bot.

## Requirements
1. Python 3.5+
2. docker-ce (as provided by docker package repos)
3. docker-compose (as provided by PyPI)

## Recommendations
Usage of [virtualenv](https://realpython.com/blog/python/python-virtual-environments-a-primer/) is recommended for package library / runtime isolation.

## Usage
To run the server, please execute the following from the root directory:

1. Setup virtual environment
```bash
python3 -venv env
source env/bin/activate
```

2. Install dependencies
```bash
pip3 install -r requirements.txt
```
    
3. Copy `__init__.template.py` to `__init__.py` with correct values

4. Run Startup server as python module
```bash
python3 -m hackupc.bienebot
```
    
## Deploy

via docker-compose
```bash
docker-compose up -d --build && docker image prune -f
```

## Log

Run logs from docker-compose once it's up and running
```bash
docker-compose logs -f --timestamps bienebot
```