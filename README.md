# GitHub Redis Project

This Python application uses Redis to store and manage repository data from the provided GitHub Archive dataset.

## Features

- Imports repository data from `Sample_Repos.json`
- Creates repository records
- Reads repository records
- Updates watcher counts
- Deletes repository records

## Requirements

- Python 3
- Redis
- Python `redis` library
- WSL / Ubuntu

## Run the Program

Start Redis in WSL:

```bash
redis-server --daemonize yes
```

Check the Redis connection:

```bash
redis-cli ping
```

A successful connection should return:

```text
PONG
```

Then run the program:

```bash
python3 main.py
```

Use the numbered menu options to import data and perform CRUD operations.
