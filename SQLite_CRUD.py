# Name: Max Ramos
# Date: 10/03/2026
# Option: SQLite
# Summary:
# This program reads GitHub repository data from a JSON file and stores
# the information in an SQLite database. The user can perform CRUD
# operations and view several features that analyze repository watch counts.

import sqlite3
import json
import os

DATABASE_NAME = "GitHubArchive.db"
JSON_FILE = "Sample_Repos.json"


# Connect to the SQLite database
def connect_database():
    return sqlite3.connect(DATABASE_NAME)


# Create the repositories table
def create_table():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS repositories (
            repo_name TEXT PRIMARY KEY,
            watch_count INTEGER
        )
    """)

    conn.commit()
    conn.close()


# Import JSON data into the database
def import_json():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM repositories")
    count = cursor.fetchone()[0]

    # Prevent the dataset from being imported every time the program runs
    if count > 0:
        print("\nData has already been imported.")
        conn.close()
        return

    if not os.path.exists(JSON_FILE):
        print(f"\n{JSON_FILE} was not found.")
        conn.close()
        return

    print("\nImporting data. Please wait...")

    with open(JSON_FILE, "r", encoding="utf-8") as file:
        for line in file:
            data = json.loads(line)

            repo_name = data["repo_name"]
            watch_count = int(data["watch_count"])

            cursor.execute("""
                INSERT INTO repositories (repo_name, watch_count)
                VALUES (?, ?)
            """, (repo_name, watch_count))

    conn.commit()
    conn.close()

    print("Data imported successfully.")


# CREATE
def add_repository():
    repo_name = input("\nEnter repository name: ")
    
    try:
        watch_count = int(input("Enter watch count: "))
    except ValueError:
        print("Watch count must be a number.")
        return

    conn = connect_database()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO repositories (repo_name, watch_count)
            VALUES (?, ?)
        """, (repo_name, watch_count))

        conn.commit()
        print("Repository added successfully.")

    except sqlite3.IntegrityError:
        print("That repository already exists.")

    conn.close()


# READ
def view_repository():
    repo_name = input("\nEnter repository name: ")

    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT repo_name, watch_count
        FROM repositories
        WHERE repo_name = ?
    """, (repo_name,))

    result = cursor.fetchone()

    if result:
        print("\nRepository:", result[0])
        print("Watch Count:", result[1])
    else:
        print("Repository not found.")

    conn.close()


# UPDATE
def update_repository():
    repo_name = input("\nEnter repository name to update: ")

    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT repo_name
        FROM repositories
        WHERE repo_name = ?
    """, (repo_name,))

    result = cursor.fetchone()

    if not result:
        print("Repository not found.")
        conn.close()
        return

    try:
        new_watch_count = int(input("Enter new watch count: "))
    except ValueError:
        print("Watch count must be a number.")
        conn.close()
        return

    cursor.execute("""
        UPDATE repositories
        SET watch_count = ?
        WHERE repo_name = ?
    """, (new_watch_count, repo_name))

    conn.commit()
    conn.close()

    print("Repository updated successfully.")


# DELETE
def delete_repository():
    repo_name = input("\nEnter repository name to delete: ")

    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM repositories
        WHERE repo_name = ?
    """, (repo_name,))

    if cursor.rowcount > 0:
        print("Repository deleted successfully.")
    else:
        print("Repository not found.")

    conn.commit()
    conn.close()


# FEATURE 1
# Display the ten repositories with the highest watch counts
def top_repositories():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT repo_name, watch_count
        FROM repositories
        ORDER BY watch_count DESC
        LIMIT 10
    """)

    results = cursor.fetchall()

    print("\nTop 10 Repositories by Watch Count")
    print("----------------------------------")

    for repo in results:
        print(f"{repo[0]} - {repo[1]} watches")

    conn.close()


# FEATURE 2
# Display the average watch count
def average_watch_count():
    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT AVG(watch_count)
        FROM repositories
    """)

    result = cursor.fetchone()[0]

    print(f"\nAverage Watch Count: {result:.2f}")

    conn.close()


# FEATURE 3
# Count repositories at or above a user-entered watch count
def watch_count_search():
    try:
        minimum = int(input("\nEnter minimum watch count: "))
    except ValueError:
        print("Watch count must be a number.")
        return

    conn = connect_database()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM repositories
        WHERE watch_count >= ?
    """, (minimum,))

    result = cursor.fetchone()[0]

    print(f"\nRepositories with at least {minimum} watches: {result}")

    conn.close()


# Main menu
def main():
    create_table()

    while True:
        print("\nGitHub Repository Database")
        print("--------------------------")
        print("1. Import JSON Data")
        print("2. Add Repository")
        print("3. View Repository")
        print("4. Update Repository")
        print("5. Delete Repository")
        print("6. Display Top 10 Repositories")
        print("7. Display Average Watch Count")
        print("8. Count Repositories by Minimum Watch Count")
        print("9. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            import_json()

        elif choice == "2":
            add_repository()

        elif choice == "3":
            view_repository()

        elif choice == "4":
            update_repository()

        elif choice == "5":
            delete_repository()

        elif choice == "6":
            top_repositories()

        elif choice == "7":
            average_watch_count()

        elif choice == "8":
            watch_count_search()

        elif choice == "9":
            print("\nProgram closed.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()