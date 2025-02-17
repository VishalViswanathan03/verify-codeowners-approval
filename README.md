# Verify CODEOWNERS Approval

## Overview

The **Verify CODEOWNERS Approval** GitHub Action ensures that a pull request (PR) meets the required number of approvals from CODEOWNERS before merging. This action:
- Fetches the list of **CODEOWNERS** for the modified files.
- Verifies if the **minimum required approvals** have been met.
- Ensures compliance with repository **CODEOWNERS policies**.

## Features
- **Automatic PR Verification**: Runs the checks whenever a PR is opened or updated.
- **CODEOWNERS Compliance**: Ensures that only authorized owners approve changes.
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

### **GitHub Workflow File (`.github/workflows/verify-codeowners-approval.yml`)**

```yaml
name: Verify CODEOWNERS Approval

on:
  pull_request:
    branches:
      - main

jobs:
  verify:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Verify CODEOWNERS Approval
        uses: your-org/verify-codeowners-approval-action@v1
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
│   │   ├── verify-codeowners-approval.yml
│   ├── CODEOWNERS
├── action.yml
├── Dockerfile
├── requirements.txt
├── main.py
├── README.md
```

---

## Installation and Setup
1. **Add the action to your repository** under `.github/workflows/verify-codeowners-approval.yml`.
2. **Provide the required `GITHUB_TOKEN`** in your workflow.
3. **Customize `min_approval` if needed**.
4. **Ensure your repository has a `CODEOWNERS` file**.

---

## How It Works
- The **Python script (`main.py`)** checks the approvals from CODEOWNERS.
- The **GitHub API** is used to verify the PR approvals.

---

## Branding
- **Icon**: `check-circle`
- **Color**: `blue`

---

## License
This action is released under the **MIT License**.

