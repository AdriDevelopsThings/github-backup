#!/usr/bin/env python
from argparse import ArgumentParser
from os import environ, mkdir
from os.path import join, exists
from subprocess import Popen

import requests

try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass

parser = ArgumentParser(description="Backup all GitHub repositories")
parser.add_argument("-o", "--output-directory", type=str, default="output")
parser.add_argument("--use-http", action="store_true", help="Use HTTP cloning instead of ssh cloning")

GITHUB_ACCESS_TOKEN = environ["GITHUB_ACCESS_TOKEN"]

def __github_get(url):
    response = requests.get(
        url,
        headers={
            "Authorization": "Bearer " + GITHUB_ACCESS_TOKEN
        }
    )
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    args = parser.parse_args()
    if not exists(args.output_directory):
        mkdir(args.output_directory)

    me = __github_get("https://api.github.com/user")
    repos = __github_get(me["repos_url"])
    for repo in repos:
        name = repo["name"]
        full_name = repo["full_name"]
        path = join(args.output_directory, name)
        if exists(path):
            Popen(["git", "fetch", "--all"], cwd=path).wait()
        else:
            url = "git@github.com:" + full_name
            if args.use_http:
                url = "https://github.com/" + full_name
            Popen(["git", "clone", "--mirror", url, path]).wait()
