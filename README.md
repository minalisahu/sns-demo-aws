# SNS Demo - AWS SAM + Python

This project demonstrates how to build a serverless application using **AWS SAM**, **Python**, and **Amazon SNS**. It exposes an HTTP POST endpoint via **API Gateway** to publish messages to an SNS topic.

## 🛠 Tech Stack
- AWS Lambda (Python 3.12)
- Amazon SNS
- AWS SAM (Serverless Application Model)
- API Gateway

## 📦 Features
- Publishes messages to a named SNS topic
- Configurable via `template.yaml`
- Easily deployable with `sam deploy`

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/sns-demo-aws.git
cd sns-demo-aws
```
### 2. 🚀 Build and Deploy
# Step 1: Build the SAM application
sam build

# Step 2: Deploy with guided prompts (only required the first time)
sam deploy --guided

#  3. Test with curl
curl -X POST https://your-api-id.execute-api.region.amazonaws.com/Prod/publish \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello from SNS via SAM!"}'

#  4.🧹 Cleanup
aws cloudformation delete-stack --stack-name sns-demo-aws

#  5 .aws sns subscribe \
--topic-arn arn:aws:sns:<region>:<account-id>:SNS-DEMO \
--protocol email \
--notification-endpoint your_email@example.com
