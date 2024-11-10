# github-backup
Backup all of your github repositories.

## Installation
You'll need python and have to install the dependencies with pip:
```
pip install -r requirements.txt
```

## Usage
Acquire a github token [here](https://github.com/settings/tokens) and set the token as `GITHUB_TOKEN` env variable in your shell or create a `.env` file. Now you can run
```
./main.py -o YOUR_OUTPUT_DIRECTORY
```