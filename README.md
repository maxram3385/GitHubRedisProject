# GitHub Database Project

This project uses Python and the provided GitHub Archive dataset to demonstrate different database technologies.

The same `Sample_Repos.json` dataset is used throughout the project.

---

## Week 1 - Redis

The Redis version stores and manages repository data using Redis.

### Features

- Import repository data from `Sample_Repos.json`
- Create repository records
- Read repository records
- Update watcher counts
- Delete repository records

### Requirements

- Python 3
- Redis
- Python `redis` library
- WSL / Ubuntu

### Run

Start Redis:

```bash
redis-server --daemonize yes
```

Check the connection:

```bash
redis-cli ping
```

Run the program:

```bash
python3 main.py
```

---

## Week 2 - MongoDB

The MongoDB version uses PyMongo to store and analyze repository data.

### CRUD Features

- Import repository data from `Sample_Repos.json`
- Create repository documents
- Find repository documents
- Update watcher counts
- Delete repository documents

### Additional Features

1. Display the 10 most watched repositories
2. Find repositories above a specified watch count
3. Display repository statistics, including total repositories, average watchers, highest watch count, and lowest watch count

### Requirements

- Python 3
- MongoDB
- MongoDB Compass
- Python `pymongo` library

Install PyMongo:

```bash
pip install pymongo
```

Run the program:

```bash
py MongoDBMain.py
```

---

## Project Progress

- Week 1: Redis
- Week 2: MongoDB
- Week 3: Apache Cassandra planned
