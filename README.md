# GitHub Database Project

This project uses Python and the provided GitHub Archive dataset to demonstrate the use of multiple database technologies.

The same `Sample_Repos.json` dataset is used throughout the project. The dataset contains GitHub repository names and watcher counts. Each week, the application is adapted to work with a different database system while maintaining similar CRUD and data-analysis functionality.

---

## Week 1 - Redis

The Redis version stores and manages GitHub repository data using a Redis key-value database.

### Features

- Import repository data from `Sample_Repos.json`
- Store repository information using Redis hashes
- Create repository records
- Read repository records
- Update repository watcher counts
- Delete repository records

### Technology / Dependencies

- Python 3
- Redis
- Python `redis` library
- WSL / Ubuntu

### Run

Start Redis:

redis-server --daemonize yes

Check the connection:

redis-cli ping

Run the program:

python3 main.py

---

## Week 2 - MongoDB

The MongoDB version uses PyMongo to store and analyze repository data in a document database.

### CRUD Features

- Import repository data from `Sample_Repos.json`
- Create repository documents
- Find repository documents
- Update watcher counts
- Delete repository documents

### Additional Features

1. Display the most watched repositories
   - Sorts repository records by watcher count and displays the ten repositories with the highest watcher counts.

2. Find repositories above a specified watcher count
   - Allows the user to enter a minimum watcher count and displays repositories that meet or exceed that value.

3. Display repository statistics
   - Displays the total number of repositories, average watcher count, highest watcher count, and lowest watcher count.

### Technology / Dependencies

- Python 3
- MongoDB
- PyMongo
- MongoDB Compass
- Visual Studio Code

### Run

Make sure MongoDB is running, then run the Python application:

python main.py

---

## Week 3 - Apache Cassandra

The Cassandra version stores and manages the same GitHub repository data using an Apache Cassandra column-family database.

The Python application connects to a local Cassandra server, creates the required keyspace and table, and stores repository names and watcher counts from the GitHub Archive dataset.

### Database Structure

Keyspace:

github_project

Table:

repositories

Fields:

- repo_name - TEXT PRIMARY KEY
- watch_count - INT

### CRUD Features

- Import repository data from `Sample_Repos.json`
- Create new repository records
- Find repositories by repository name
- Update repository watcher counts
- Delete repository records

The application currently imports the first 100 repository records from the JSON dataset into Cassandra.

### Additional Features

1. Display the most watched repositories
   - Retrieves repository records from Cassandra, sorts them by watcher count, and displays the ten repositories with the highest watcher counts.

2. Find repositories above a specified watcher count
   - Allows the user to enter a minimum watcher count and displays all imported repositories that meet or exceed the specified value.

3. Display repository statistics
   - Calculates and displays the total number of repositories, average watcher count, highest watcher count, and lowest watcher count.

### Technology / Dependencies

- Python 3
- Apache Cassandra
- Python `cassandra-driver` library
- Ubuntu / VCASTLE

### Cassandra Setup

Start Cassandra:

sudo systemctl start cassandra

Check Cassandra status:

sudo systemctl status cassandra

Install the Cassandra Python driver if needed:

pip install cassandra-driver

The application uses Cassandra authentication with the configured Cassandra user account.

### Run

Place both of the following files in the Cassandra directory:

main.py
Sample_Repos.json

Change into the Cassandra directory:

cd ~/Cassandra

Run the application:

python3 main.py

### Application Menu

1. Import repositories from JSON
2. Add repository
3. Find repository
4. Update repository
5. Delete repository
6. Show most watched repositories
7. Find repositories above a watcher count
8. Display repository statistics
9. Exit

---

## Current Project Features

Across the Redis, MongoDB, and Cassandra implementations, the project demonstrates:

- Reading JSON-formatted GitHub Archive data with Python
- Connecting Python applications to multiple database technologies
- Creating, reading, updating, and deleting database records
- Searching and filtering repository information
- Sorting repository data by watcher count
- Calculating statistics from stored repository data
- Using a terminal-based menu interface
- Maintaining separate database implementations while working with the same source dataset

---

## Dataset

The project uses:

Sample_Repos.json

The repository records contain:

- repo_name
- watch_count

Example:

{"repo_name":"FreeCodeCamp/FreeCodeCamp","watch_count":"90457"}

---

## Project Development

Database technologies implemented so far:

Week 1 - Redis
Week 2 - MongoDB
Week 3 - Apache Cassandra

Future versions of the project will continue applying additional database technologies to the same GitHub Archive dataset while maintaining and expanding the application's CRUD and data-analysis functionality.
