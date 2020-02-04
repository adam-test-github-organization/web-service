# Github Webhook Test

![Github Webhook Test Checks](https://github.com/adam-test-github-organization/web-service/workflows/Github%20Webhook%20Test%20Checks/badge.svg?branch=master)

This is a webhook that protects the master branch, when a a new repository is created.
The webhook is written in Python and deployed using the Serverless Framework on AWS.

The webhook will create some default permissions, in order to protect the master branch when created.
These permissions will be added to a new issue on the repository, with the repository owner tagged in the same issue.

## Local development and deployment (on mac enviroment)

```
# Ensure you have an AWS Account and credentials configured
brew install pip
pip install awscli
aws configure

# Install Python virtual environment
brew install pipenv

# Install Serverless framework (ensure npm is install)
npm i -g serverless

# Install Serverless dependencies
serverless plugin install --name serverless-python-requirements

# Install Python virtual environment
pipenv install --dev

# Ensure enviornment variables are set up
cp .env.sample .env

# Update GITHUB_WEBHOOK_SECRET & GITHUB_TOKEN inside .env

# Run virtual environment
pipenv shell

# Deploy Serverless Webservice
serverless deploy
```

The following is an example of a serverless deployment:

```
(web-service) bash-3.2$ serverless deploy
Serverless: Generating requirements.txt from Pipfile...
Serverless: Adding Python requirements helper...
Serverless: Parsed requirements.txt from Pipfile in XXXXXX/web-service/.serverless/requirements.txt...
Serverless: Installing requirements from XXXXXX/Library/Caches/serverless-python-requirements/72e8d4f17fc2da08f4d9625ebc494431d31122f19f67fc5b440a5bd5397e4722_slspyc/requirements.txt ...
Serverless: Docker Image: lambci/lambda:build-python3.7
Serverless: Using download cache directory XXXXXX/Library/Caches/serverless-python-requirements/downloadCacheslspyc
Serverless: Running docker run --rm -v XXXXXX/Library/Caches/serverless-python-requirements/72e8d4f17fc2da08f4d9625ebc494431d31122f19f67fc5b440a5bd5397e4722_slspyc\:/var/task\:z -v XXXXXX/Library/Caches/serverless-python-requirements/downloadCacheslspyc\:/var/useDownloadCache\:z -u 0 lambci/lambda\:build-python3.7 /bin/sh -c 'python3.7 -m pip install -t /var/task/ -r /var/task/requirements.txt --cache-dir /var/useDownloadCache && find /var/task -name \\*.so -exec strip \\{\\} \\;'...
Serverless: Zipping required Python packages...
Serverless: Packaging service...
Serverless: Excluding development dependencies...
Serverless: Removing Python requirements helper...
Serverless: Injecting required Python packages to package...
Serverless: WARNING: Function github_webhook_protect_master has timeout of 900 seconds, however, it's attached to API Gateway so it's automatically limited to 30 seconds.
Serverless: Uploading CloudFormation file to S3...
Serverless: Uploading artifacts...
Serverless: Uploading service github-webhook-listeners.zip file to S3 (471.63 KB)...
Serverless: Validating template...
Serverless: Updating Stack...
Serverless: Checking Stack update progress...
..............
Serverless: Stack update finished...
Service Information
service: github-webhook-listeners
stage: dev
region: ap-southeast-2
stack: github-webhook-listeners-dev
resources: 12
api keys:
  None
endpoints:
  POST - https://n9s6eff6v0.execute-api.ap-southeast-2.amazonaws.com/dev/webhook
functions:
  github_webhook_protect_master: github-webhook-listeners-dev-github_webhook_protect_master
layers:
  None
```

## Testing
```
pipenv run fab check test
```
