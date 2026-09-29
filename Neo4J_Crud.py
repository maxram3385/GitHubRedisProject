# ---------------------------------------------------------
# Name: Max Ramos
# Assignment: Neo4j CRUD Application
# Description: This program reads repository data from a
# JSON file, stores it in Neo4j, and performs CRUD
# operations and basic data analysis.
# ---------------------------------------------------------

import json
from neo4j import GraphDatabase


# Neo4j connection information
URI = "neo4j://localhost:7687"
AUTH = ("neo4j", "password1")


# Connect to Neo4j
driver = GraphDatabase.driver(URI, auth=AUTH)
session = driver.session()


# ---------------------------------------------------------
# LOAD JSON DATA
# ---------------------------------------------------------

def loadData():

    file = open("Sample_Repos (1).json", "r", encoding="utf-8")

    count = 0

    for line in file:

        if count == 100:
            break

        repo = json.loads(line)

        repoName = repo["repo_name"]
        watchCount = repo["watch_count"]

        query = """
        MERGE (r:Repository {repo_name: $repoName})
        SET r.watch_count = $watchCount
        """

        session.run(
            query,
            repoName=repoName,
            watchCount=int(watchCount)
        )

        count += 1

    file.close()

    print(count, "repositories added to Neo4j.")


# ---------------------------------------------------------
# CREATE
# ---------------------------------------------------------

def createRepo():

    repoName = input("Enter repository name: ")
    watchCount = int(input("Enter watch count: "))

    query = """
    CREATE (r:Repository {
        repo_name: $repoName,
        watch_count: $watchCount
    })
    """

    session.run(
        query,
        repoName=repoName,
        watchCount=watchCount
    )

    print("Repository created.")


# ---------------------------------------------------------
# READ
# ---------------------------------------------------------

def readRepo():

    repoName = input("Enter repository name: ")

    query = """
    MATCH (r:Repository {repo_name: $repoName})
    RETURN r.repo_name, r.watch_count
    """

    result = session.run(
        query,
        repoName=repoName
    )

    for record in result:
        print("Repository:", record["r.repo_name"])
        print("Watch Count:", record["r.watch_count"])


# ---------------------------------------------------------
# UPDATE
# ---------------------------------------------------------

def updateRepo():

    repoName = input("Enter repository name: ")
    watchCount = int(input("Enter new watch count: "))

    query = """
    MATCH (r:Repository {repo_name: $repoName})
    SET r.watch_count = $watchCount
    RETURN r.repo_name, r.watch_count
    """

    result = session.run(
        query,
        repoName=repoName,
        watchCount=watchCount
    )

    for record in result:
        print("Repository:", record["r.repo_name"])
        print("New Watch Count:", record["r.watch_count"])


# ---------------------------------------------------------
# DELETE
# ---------------------------------------------------------

def deleteRepo():

    repoName = input("Enter repository name: ")

    query = """
    MATCH (r:Repository {repo_name: $repoName})
    DELETE r
    """

    session.run(
        query,
        repoName=repoName
    )

    print("Repository deleted.")


# ---------------------------------------------------------
# FEATURE 1
# TOP 10 MOST WATCHED REPOSITORIES
# ---------------------------------------------------------

def topRepos():

    query = """
    MATCH (r:Repository)
    RETURN r.repo_name, r.watch_count
    ORDER BY r.watch_count DESC
    LIMIT 10
    """

    result = session.run(query)

    print("\nTop 10 Most Watched Repositories")

    for record in result:
        print(
            record["r.repo_name"],
            "-",
            record["r.watch_count"]
        )


# ---------------------------------------------------------
# FEATURE 2
# LONGEST REPOSITORY NAME
# ---------------------------------------------------------

def longestRepo():

    query = """
    MATCH (r:Repository)
    RETURN r.repo_name, size(r.repo_name) AS nameLength
    ORDER BY nameLength DESC
    LIMIT 1
    """

    result = session.run(query)

    for record in result:
        print("\nLongest Repository Name:")
        print(record["r.repo_name"])
        print("Length:", record["nameLength"])


# ---------------------------------------------------------
# FEATURE 3
# WATCH COUNT STATISTICS
# ---------------------------------------------------------

def watchStats():

    query = """
    MATCH (r:Repository)
    RETURN
    max(r.watch_count) AS highest,
    min(r.watch_count) AS lowest,
    avg(r.watch_count) AS average
    """

    result = session.run(query)

    for record in result:
        print("\nWatch Count Statistics")
        print("Highest:", record["highest"])
        print("Lowest:", record["lowest"])
        print("Average:", record["average"])


# ---------------------------------------------------------
# MAIN PROGRAM
# ---------------------------------------------------------

print("Connecting to Neo4j...")

loadData()

choice = ""

while choice != "8":

    print("\nNeo4j Repository Menu")
    print("1. Create Repository")
    print("2. Read Repository")
    print("3. Update Repository")
    print("4. Delete Repository")
    print("5. Top 10 Most Watched Repositories")
    print("6. Longest Repository Name")
    print("7. Watch Count Statistics")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        createRepo()

    elif choice == "2":
        readRepo()

    elif choice == "3":
        updateRepo()

    elif choice == "4":
        deleteRepo()

    elif choice == "5":
        topRepos()

    elif choice == "6":
        longestRepo()

    elif choice == "7":
        watchStats()

    elif choice == "8":
        print("Program closed.")

    else:
        print("Invalid choice.")


# Close connection
session.close()
driver.close()
