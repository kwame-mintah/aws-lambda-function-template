# AWS Lambda Function Template

[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/downloads/release/python-3121/)
<a href="https://github.com/new?template_name=aws-lambda-function-template&template_owner=kwame-mintah">
  <img src="https://img.shields.io/badge/use%20this-template-blue?logo=github">
</a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>

This is a template project for a AWS Lambda function deployed as a docker image.

This repository is intended as a quick-start and includes the following:

- A `Dockerfile` to build the lambda function
- GitHub Actions to build and push the image to an AWS Elastic Container Registry (ECR)
- Pre-commit hooks to run on each commit
- Example unit and feature tests

## Development

### Dependencies

- [Python](https://www.python.org/downloads/release/python-3121/)
- [Docker for Desktop](https://www.docker.com/products/docker-desktop/)
- [Amazon Web Services](https://aws.amazon.com/?nc2=h_lg)

## Usage

1. Build the docker image locally:

   ```commandline
   docker build --no-cache -t aws_lambda:local .
   ```

2. Run the docker image built:

   ```commandline
   docker run --platform linux/amd64 -p 9000:8080 aws_lambda:local
   ```

3. Send an event to the lambda via curl:
   ```commandline
   curl "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{<REPLACE_WITH_JSON_BELOW>}'
   ```
   ```json
   {
     "Records": [
       {
         "eventVersion": "2.0",
         "eventSource": "aws:s3",
         "awsRegion": "us-east-1",
         "eventTime": "1970-01-01T00:00:00.000Z",
         "eventName": "ObjectCreated:Put",
         "userIdentity": { "principalId": "EXAMPLE" },
         "requestParameters": { "sourceIPAddress": "127.0.0.1" },
         "responseElements": {
           "x-amz-request-id": "EXAMPLE123456789",
           "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
         },
         "s3": {
           "s3SchemaVersion": "1.0",
           "configurationId": "testConfigRule",
           "bucket": {
             "name": "example-bucket",
             "ownerIdentity": { "principalId": "EXAMPLE" },
             "arn": "arn:aws:s3:::example-bucket"
           },
           "object": {
             "key": "test%2Fkey",
             "size": 1024,
             "eTag": "0123456789abcdef0123456789abcdef",
             "sequencer": "0A1B2C3D4E5F678901"
           }
         }
       }
     ]
   }
   ```

## GitHub Action (CI/CD)

The GitHub Action "🚀 Push Docker image to AWS ECR" will checkout the repository and push a docker image to the chosen AWS ECR using
[configure-aws-credentials](https://github.com/aws-actions/configure-aws-credentials/tree/v4.0.1/) action. The following repository secrets need to be set:

| Secret             | Description                  |
| ------------------ | ---------------------------- |
| AWS_REGION         | The AWS Region.              |
| AWS_ACCOUNT_ID     | The AWS account ID.          |
| AWS_ECR_REPOSITORY | The AWS ECR repository name. |
