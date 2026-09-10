import json
import redis

# Connect to Redis
r = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True,
    socket_connect_timeout=3,
    socket_timeout=3
)


def create_repository():
    name = input("Repository name: ")
    watchers = input("Watcher count: ")

    key = "repo:" + name

    r.hset(
        key,
        mapping={
            "repo_name": name,
            "watch_count": watchers
        }
    )

    print("Repository added.")


def read_repository():
    name = input("Repository name: ")
    key = "repo:" + name

    repo = r.hgetall(key)

    if repo:
        print("Repository:", repo["repo_name"])
        print("Watchers:", repo["watch_count"])
    else:
        print("Repository not found.")


def update_repository():
    name = input("Repository name: ")
    key = "repo:" + name

    if r.exists(key):
        watchers = input("New watcher count: ")

        r.hset(key, "watch_count", watchers)

        print("Repository updated.")
    else:
        print("Repository not found.")


def delete_repository():
    name = input("Repository name: ")
    key = "repo:" + name

    if r.delete(key):
        print("Repository deleted.")
    else:
        print("Repository not found.")


def import_repositories():
    file_path = "GitHubArchive-Dataset/Sample_Repos.json"

    count = 0

    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:

            repo = json.loads(line)

            name = repo["repo_name"]
            watchers = repo["watch_count"]

            key = "repo:" + name

            r.hset(
                key,
                mapping={
                    "repo_name": name,
                    "watch_count": watchers
                }
            )

            count += 1

            # Only import 100 for now
            if count >= 100:
                break

    print(count, "repositories imported.")


def main():
    print("Redis connection:", r.ping())

    while True:
        print("\nGitHub Repository Database")
        print("1. Import repositories from JSON")
        print("2. Add repository")
        print("3. Find repository")
        print("4. Update repository")
        print("5. Delete repository")
        print("6. Exit")

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
            print("Goodbye.")
            break

        else:
            print("Invalid option.")


main()
