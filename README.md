# Database Project

This project uses Python to demonstrate working with multiple database technologies, including Redis, MongoDB, and Apache Cassandra.

The Redis and MongoDB portions use the provided `Sample_Repos.json` GitHub Archive dataset. The Cassandra portion uses the provided `dataset_en_dev.json` Amazon review dataset.

---

## Week 1 - Redis

The Redis version stores and manages repository data using Redis.

### Python File

`main.py`

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

### Python File

`MongoDBMain.py`

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

## Week 3 - Apache Cassandra

The Cassandra version uses the Python `cassandra-driver` library to create and manage an Amazon review database using CRUD operations.

### Python File

`amazonCRUD.py`

### Dataset

`dataset_en_dev.json`

### Database Structure

The application creates an `Amazon` keyspace containing two tables:

- `Reviews`
- `ProductCategories`

The `Reviews` table stores:

- Review ID
- Product ID
- Reviewer ID
- Star rating
- Review body
- Review title
- Product category

The `ProductCategories` table stores:

- Product ID
- Star rating
- Language
- Product category

### Features

- Connect to a local Apache Cassandra database
- Create the `Amazon` keyspace
- Create the `Reviews` and `ProductCategories` tables
- Import review data from `dataset_en_dev.json`
- Display all distinct product categories
- Display the number of 4-star and higher reviews for a user-entered product category
- Display the number of 1-star reviews for a user-entered product category
- Allow the user to enter and execute custom CQL `SELECT` statements
- Add columns to the `Reviews` or `ProductCategories` tables
- Remove columns from the `Reviews` or `ProductCategories` tables
- Delete the `Reviews` and `ProductCategories` tables
- Delete the `Amazon` keyspace
- Provide an interactive menu for performing Cassandra operations

### Requirements

- Python 3
- Apache Cassandra
- Python `cassandra-driver` library
- Ubuntu / VCASTLE

Install the Cassandra driver:

```bash
pip install cassandra-driver
```

Start Cassandra:

```bash
sudo systemctl start cassandra
```

Run the program:

```bash
python3 amazonCRUD.py
```

---

## Project Progress

- Week 1: Redis - Complete
- Week 2: MongoDB - Complete
- Week 3: Apache Cassandra - Complete
