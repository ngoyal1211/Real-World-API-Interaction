import requests
import time

# Replace with your GitHub username and personal access token
username = "ngoyal1211"
token = "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"

# Base URL for GitHub API
base_url = "https://api.github.com/"

# Function to fetch the top 10 public repositories by stars
def get_top_repositories():
    # API endpoint to search for public repositories sorted by stars
    endpoint = "search/repositories"
    
    # Parameters for the search query
    params = {
        "q": "is:public",
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }
    
    # Construct the URL
    url = base_url + endpoint
    
    # Send a GET request to the API
    response = requests.get(url, auth=(username, token), params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        repositories = response.json()["items"]
        return repositories
    else:
        print("Failed to fetch repositories. Status code:", response.status_code)
        return []

# Function to fetch a recent bug issue for a repository
def get_recent_bug_issue(repo_name):
    # API endpoint to fetch issues with the "bug" label for a repository
    endpoint = f"repos/{repo_name}/issues"
    
    # Construct the URL
    url = base_url + endpoint
    
    # Send a GET request to the API
    response = requests.get(url, auth=(username, token), params={"labels": "bug"})
    
    # Check if the request was successful
    if response.status_code == 200:
        issues = response.json()
        if issues:
            bug_issue = issues[0]
            print("Bug Issue:")
            print({bug_issue['title']}, bug_issue['body'])
        else:
            print("Bug Issue:")
            print("none")
        print("--------------------------------------------------")
    else:
        print(f"Failed to fetch issues for {repo_name}. Status code:", response.status_code)

if __name__ == "__main__":
    top_repositories = get_top_repositories()
    
    if top_repositories:
        for repo in top_repositories:
            repo_name = repo["full_name"]
            stars = repo["stargazers_count"]
            print(f"{repo_name}, {stars}")
            get_recent_bug_issue(repo["full_name"])
            # Sleep for a while to avoid rate limiting (GitHub API rate limit is 60 requests per hour for unauthenticated users)
            time.sleep(6)  # Sleep for 6 seconds between requests
    else:
        print("No repositories to process.")