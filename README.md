# Data Contracts Sandbox
This repository is used to maintain and manage our data contracts. These contracts are defined using JSON schemas. 
In this example we use pre-commit hooks to validate the contracts, and GitHub Actions to automatically bump the version when changes are pushed to the master branch.

In a production setting you could do far more sophisticated things i.e, 
* In the pre-commit activities you could 
  - Lookup in the company AD to see if the dataOwner exists and fire warnings if not
  - Validate the contract :) 
* In the actions you could parse the contract (with a `parser.py` script) and automatatically send changes to downstream services that utilise the metadata
  - Data governance and when fields change in there access control 
  - Data discoverability and updating the meta information used by these services)
  - Create / evolve schema registry entries 
  - Create / evolve catalog entries

## Prerequisites

- Python 3.7 or later
- git for version control
- GitHub account for managing the repository

## Repository Structure

The repository has the following structure:
```
.
├── LICENSE
├── README.md
├── contract_schema.json
├── test_contract.json
├── validate.py
└── github_actions/version_bump.yaml 
```

- `LICENSE`: The license for this repository.
- `README.md`: This document, which provides an overview of the repository.
- `contract_schema.json`: The JSON schema for our data contracts.
- `test_contract.json`: A sample data contract that conforms to our schema.
- `validate.py`: The Python script that validates our data contracts against the schema.
- `github_actions/version_bump.yaml` The yaml script for version bumping when we commit to the repo 

## JSON Schemas and Data Contracts

Our data contracts are defined using JSON schemas. These schemas provide a clear and concise definition of the structure and type of data that our contracts should have. 

The contracts themselves are JSON documents that conform to the structure defined in the schema.

## Pre-commit Validation

We use a pre-commit hook to validate our data contracts. This hook runs every time you make a commit. It checks that the changes you've made to the contracts are valid according to the schema.

To set up the pre-commit hook, follow these steps:
Create a shell script named `pre-commit` in the `.git/hooks/` directory of your repository. This script will be executed every time you try to commit changes.

```bash
#!/bin/sh

python validate.py

if [ $? -ne 0 ]; then
 echo "Data validation failed, commit rejected"
 exit 1
fi
```
Make the pre-commit hook executable by running `chmod +x .git/hooks/pre-commit`.

## Automatic Version Bumping

We use a GitHub Action to automatically bump the version of our contracts when changes are pushed to the master branch. 
The configuration for this action can be found in `github_actions/version_bump.yaml`.

The following action must be taken to add this to the repo

**Create a new GitHub Action**: In your GitHub repository, navigate to the "Actions" tab and click on "New Workflow". If you have no existing workflows, you can also click on "Set up a workflow yourself".

**Set up the workflow**: In the new workflow file, you will need to set up the triggering event and the jobs that the workflow will run. An example file is found `github_actions/version_bump.yaml`

In this example, the workflow triggers when you push to the master branch. The job it runs checks out your code and then uses the github-tag-action to automatically bump the version and push a new tag.

**Configure the action**: The github-tag-action can be configured with several environment variables. Here are some of the most commonly used ones:
  - GITHUB_TOKEN (required): This is required for the action to have permission to push the new tag to your repository. The token is provided by GitHub, you just need to reference it as shown above.
  - DEFAULT_BUMP (optional): Which type of version bump to use if none is explicitly provided in the commit message (major, minor, or patch). Defaults to minor.
  - WITH_V (optional): Whether or not to prefix the tag with 'v'. If true, your tags will look like v1.0.0. If false, they will look like 1.0.0.
  - 
**Commit and push the workflow**: Once you have configured the workflow to your liking, commit and push it to your repository. The workflow will now trigger according to the event you specified.


