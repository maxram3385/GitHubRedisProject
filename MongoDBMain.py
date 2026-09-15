# Name: Max Ramos
# Date: September 14, 2026
# Assignment: MongoDB GitHub Archive Project
# Purpose:
# This program imports GitHub repository data from a JSON file into MongoDB.
# It allows the user to perform CRUD operations and analyze repository data.

import json
import pymongo


# ---------------------------------------------------------
# CONNECT TO MONGODB
# ---------------------------------------------------------

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["GitHubDatabase"]

collection = db["Repositories"]


# ---------------------------------------------------------
# CREATE
# Add a new repository to MongoDB
# ---------------------------------------------------------

def create_repository():

    name = input("Repository name: ")

    watchers = input("Watcher count: ")

    try:
        watchers = int(watchers)
    except ValueError:
        print("Watcher count must be a number.")
        return

    repository = {
        "repo_name": name,
        "watch_count": watchers
    }

    collection.insert_one(repository)

    print("Repository added.")


# ---------------------------------------------------------
# READ
# Find a repository in MongoDB
# ---------------------------------------------------------

def read_repository():

    name = input("Repository name: ")

    repo = collection.find_one(
        {"repo_name": name}
    )

    if repo:

        print("Repository:", repo["repo_name"])
        print("Watchers:", repo["watch_count"])

    else:

        print("Repository not found.")


# ---------------------------------------------------------
# UPDATE
# Update the watcher count for a repository
# ---------------------------------------------------------

def update_repository():

    name = input("Repository name: ")

    repo = collection.find_one(
        {"repo_name": name}
    )

    if repo:

        watchers = input("New watcher count: ")

        try:
            watchers = int(watchers)
        except ValueError:
            print("Watcher count must be a number.")
            return

        collection.update_one(
            {"repo_name": name},
            {"$set": {"watch_count": watchers}}
        )

        print("Repository updated.")

    else:

        print("Repository not found.")


# ---------------------------------------------------------
# DELETE
# Delete a repository from MongoDB
# ---------------------------------------------------------

def delete_repository():

    name = input("Repository name: ")

    result = collection.delete_one(
        {"repo_name": name}
    )

    if result.deleted_count > 0:

        print("Repository deleted.")

    else:

        print("Repository not found.")


# ---------------------------------------------------------
# IMPORT JSON DATA
# Import GitHub Archive repository records into MongoDB
# ---------------------------------------------------------

def import_repositories():

    file_path = "Sample_Repos.json"

    count = 0

    with open(file_path, "r", encoding="utf-8") as file:

        for line in file:

            repo = json.loads(line)

            name = repo["repo_name"]

            try:
                watchers = int(repo["watch_count"])
            except (ValueError, TypeError):
                watchers = 0

            repository = {
                "repo_name": name,
                "watch_count": watchers
            }

            # Upsert prevents duplicate repositories
            collection.update_one(
                {"repo_name": name},
                {"$set": repository},
                upsert=True
            )

            count += 1

            # Use the same 100-record sample from Week 1
            if count >= 100:
                break

    print(count, "repositories imported.")


# ---------------------------------------------------------
# FEATURE 1
# Display the 10 most watched repositories
# ---------------------------------------------------------

def show_most_watched():

    print("\nTop 10 Most Watched Repositories")

    repositories = collection.find().sort(
        "watch_count",
        pymongo.DESCENDING
    ).limit(10)

    for repo in repositories:

        print(
            repo["repo_name"],
            "-",
            repo["watch_count"],
            "watchers"
        )


# ---------------------------------------------------------
# FEATURE 2
# Find repositories above a watcher count chosen by the user
# ---------------------------------------------------------

def find_above_watchers():

    watchers = input("Minimum watcher count: ")

    try:
        watchers = int(watchers)
    except ValueError:
        print("Watcher count must be a number.")
        return

    repositories = collection.find(
        {"watch_count": {"$gte": watchers}}
    ).sort(
        "watch_count",
        pymongo.DESCENDING
    )

    print(
        "\nRepositories with at least",
        watchers,
        "watchers:"
    )

    found = False

    for repo in repositories:

        found = True

        print(
            repo["repo_name"],
            "-",
            repo["watch_count"],
            "watchers"
        )

    if not found:

        print("No repositories found.")


# ---------------------------------------------------------
# FEATURE 3
# Display statistics about the repository dataset
# ---------------------------------------------------------

def repository_statistics():

    total = collection.count_documents({})

    if total == 0:

        print("No repository data has been imported.")

        return

    pipeline = [
        {
            "$group": {
                "_id": None,
                "average_watchers": {
                    "$avg": "$watch_count"
                },
                "highest_watchers": {
                    "$max": "$watch_count"
                },
                "lowest_watchers": {
                    "$min": "$watch_count"
                }
            }
        }
    ]

    results = list(collection.aggregate(pipeline))

    stats = results[0]

    print("\nRepository Statistics")

    print("Total repositories:", total)

    print(
        "Average watchers:",
        round(stats["average_watchers"], 2)
    )

    print(
        "Highest watcher count:",
        stats["highest_watchers"]
    )

    print(
        "Lowest watcher count:",
        stats["lowest_watchers"]
    )


# ---------------------------------------------------------
# MAIN MENU
# ---------------------------------------------------------

def main():

    print("MongoDB connection successful.")

    while True:

        print("\nGitHub Repository Database")

        print("1. Import repositories from JSON")
        print("2. Add repository")
        print("3. Find repository")
        print("4. Update repository")
        print("5. Delete repository")
        print("6. Show most watched repositories")
        print("7. Find repositories above watcher count")
        print("8. Show repository statistics")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":

            import_repositories()

        elif choice == "2":

            create_repository()

        elif choice == "3":

            read_repository()

        elif choice == "4":

            update_repository()

        elif choice == "5":

            delete_repository()

        elif choice == "6":

            show_most_watched()

        elif choice == "7":

            find_above_watchers()

        elif choice == "8":

            repository_statistics()

        elif choice == "9":

            print("Goodbye.")

            break

        else:

            print("Invalid option.")


main()