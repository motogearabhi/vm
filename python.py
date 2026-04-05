import requests
from requests.auth import HTTPBasicAuth

org = "your-org"
project = "your-project"
pat = "your-pat"

base_url = f"https://dev.azure.com/{org}/{project}/_apis/git"

auth = HTTPBasicAuth('', pat)

# Get repositories
repos_url = f"{base_url}/repositories?api-version=7.0"
repos = requests.get(repos_url, auth=auth).json()

for repo in repos['value']:
    repo_id = repo['id']
    repo_name = repo['name']
    
    commits_url = f"{base_url}/repositories/{repo_id}/commits?$top=1&api-version=7.0"
    commits = requests.get(commits_url, auth=auth).json()
    
    if commits['value']:
        last_commit_date = commits['value'][0]['committer']['date']
    else:
        last_commit_date = "No commits"
    
    print(f"{repo_name}: {last_commit_date}")
