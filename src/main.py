import os
import sys
import requests

GITHUB_API_URL = "https://api.github.com"

def get_codeowners(path=".github/CODEOWNERS"):
    """Parses the CODEOWNERS file and returns a dictionary of file patterns to owners."""
    codeowners = {}
    if not os.path.exists(path):
        print(f"CODEOWNERS file not found at {path}. Skipping check.")
        return codeowners

    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                parts = line.split()
                pattern, owners = parts[0], parts[1:]
                codeowners[pattern] = owners
    return codeowners

def get_team_members(org, team_slug, token):
    """Fetches members of a GitHub team."""
    headers = {"Authorization": f"Bearer {token}", "Accept": "application/vnd.github.v3+json"}
    url = f"{GITHUB_API_URL}/orgs/{org}/teams/{team_slug}/members"
    
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return {member["login"] for member in response.json()}
    
    print(f"Failed to fetch members of team {team_slug}: {response.json()}")
    return set()

def get_pr_details(repo, pr_number, token):
    """Fetch PR details including changed files and approvals."""
    headers = {"Authorization": f"Bearer {token}"}

    # Get changed files
    files_url = f"{GITHUB_API_URL}/repos/{repo}/pulls/{pr_number}/files"
    files_response = requests.get(files_url, headers=headers)
    files = [file["filename"] for file in files_response.json()] if files_response.status_code == 200 else []

    # Get approvals
    reviews_url = f"{GITHUB_API_URL}/repos/{repo}/pulls/{pr_number}/reviews"
    reviews_response = requests.get(reviews_url, headers=headers)
    approvals = {review["user"]["login"] for review in reviews_response.json() if review["state"] == "APPROVED"} if reviews_response.status_code == 200 else set()

    return files, approvals

def main():
    token = os.getenv("INPUT_GITHUB_TOKEN")
    repo = os.getenv("GITHUB_REPOSITORY")
    pr_number = os.getenv("INPUT_PR_NUMBER")
    min_approvals = int(os.getenv("INPUT_MIN_APPROVALS", "1"))
    codeowners_path = os.getenv("INPUT_CODEOWNERS_PATH", ".github/CODEOWNERS")

    if not token:
        print("Error: GitHub token is required.")
        sys.exit(1)
    if not repo:
        print("Error: Repository information is required.")
        sys.exit(1)
    if not pr_number or not pr_number.isdigit():
        print("Error: Valid PR number is required.")
        sys.exit(1)

    pr_files, pr_approvals = get_pr_details(repo, pr_number, token)
    codeowners = get_codeowners(codeowners_path)

    required_owners = set()
    team_members = {}

    for file in pr_files:
        for pattern, owners in codeowners.items():
            if pattern in file:
                for owner in owners:
                    if owner.startswith("@"):
                        org, team_slug = owner[1:].split("/")
                        if owner not in team_members:
                            team_members[owner] = get_team_members(org, team_slug, token)
                        required_owners.update(team_members[owner])
                    else:
                        required_owners.add(owner)

    approved_count = sum(1 for owner in required_owners if owner in pr_approvals)
    approval_met = approved_count >= min_approvals

    output_path = os.getenv("GITHUB_OUTPUT")
    if output_path:
        with open(output_path, "a") as output_file:
            output_file.write(f"approval_met={str(approval_met).lower()}\n")

    print(f"Approval requirement met: {approval_met}")
    sys.exit(0)

if __name__ == "__main__":
    main()