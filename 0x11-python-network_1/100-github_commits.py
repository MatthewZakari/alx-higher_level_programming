#!/usr/bin/python3
"""
Script that lists 10 commits (from the most recent to oldest) of a repository
by a given user using the GitHub API.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./github_commits.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Failed to fetch commits: {response.status_code}")
        sys.exit(1)

    commits = response.json()[:10]
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")

