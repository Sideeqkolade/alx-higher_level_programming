#!/usr/bin/python3
""" a Python script that takes 2 arguments in order to solve this challenge.
    The first argument will be the repository name
    The second argument will be the owner name
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)
"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./100-github_commits.py <repository name> <owner name>")
        sys.exit(1)

    url = "https://api.github.com/repos/{}/{}/commits".format(
            sys.argv[1], sys.argv[2])

    response = requests.get(url)
    commits = response.json()
    for i in range(min(10, len(commits))):
        print("{}: {}".format(
            commits[i].get("sha"),
            commits[i].get("commit").get("author").get("name")))
