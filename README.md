# PR Build Check (Python + Docker)

## Overview

The **PR Build Check** GitHub Action ensures that a pull request (PR) meets the necessary build and approval requirements before merging. This action:
- Executes a **Python script** for additional validations.
- Builds and verifies a **Docker image** to ensure successful deployment.
- Checks the **minimum number of required approvals** from CODEOWNERS.

## Features
- **Automatic PR Verification**: Runs the checks whenever a PR is opened or updated.
- **CODEOWNERS Compliance**: Verifies that required approvals are met.
- **Docker Image Validation**: Ensures that the PR does not break the build.
- **Customizable Inputs**: Configure via workflow inputs.

---

## Inputs

| Input Name       | Description                                        | Required | Default Value              |
|-----------------|------------------------------------------------|----------|--------------------------|
| `github_token`   | GitHub Token for API authentication.       | ✅ Yes   | N/A                      |
| `codeowners_file` | Path to the CODEOWNERS file.                 | ❌ No   | `.github/CODEOWNERS`     |
| `pr_number`      | PR number (detected automatically).         | ❌ No   | PR event number          |
| `min_approval`   | Minimum number of required approvals.       | ❌ No   | `1`                      |

---

## Example Usage

### **GitHub Workflow File (`.github/workflows/pr-build-check.yml`)**

```yaml
name: PR Build Check (Python + Docker)

on:
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: PR Build Check
        uses: your-org/pr-build-check-action@v1
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          min_approval: 2
```

---

## Directory Structure
```
project-root/
├── .github/
│   ├── workflows/
│   │   ├── pr-build-check.yml
│   ├── CODEOWNERS
├── action.yml
├── Dockerfile
├── requirements.txt
├── main.py
├── README.md
```

---

## Installation and Setup
1. **Add the action to your repository** under `.github/workflows/pr-build-check.yml`.
2. **Provide the required `GITHUB_TOKEN`** in your workflow.
3. **Customize `min_approval` if needed**.
4. **Ensure your repository has a `CODEOWNERS` file**.

---

## How It Works
- The **Python script (`main.py`)** runs validations.
- The **Docker build process** ensures the container builds successfully.
- The **GitHub API** is used to check PR approvals.

---

## Branding
- **Icon**: `check-circle`
- **Color**: `blue`

---

## License
This action is released under the **MIT License**.

