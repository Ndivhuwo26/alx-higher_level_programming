#!/usr/bin/python3

"""a Python script that will  takes 2 arguments in order to solve this challenge."""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {
        'per_page': 10  # Retrieve 10 commits
    }
    
    response = requests.get(url, params=params)
    commits = response.json()
    
    for commit in commits:
        sha = commit['sha']
        author_name = commit['commit']['author']['name']
        print(f"{sha}: {author_name}")
