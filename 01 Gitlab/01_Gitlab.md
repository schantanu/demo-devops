# Gitlab Demo

Talk about DevOps Process
- DevOps  
- Version Control
- CI/CD

# Test Program

```
import socket
url = "www.google.com"
print("IP Address:", socket.gethostbyname(url))
```

# Create Gitlab Runner

- Get Token
- Open Runner Folder and paste token
- `docker-compose up -d`

# Gitlab YAML file

- Paste YAML code
- Get Pipeline running
- Explain YAML code

```
# Pulls Python 3.7 image from Docker Hub
image: "python:3.7"

# Check Python version and install requirements
before_script:
  - python --version
  - pip install -r requirements.txt

# Stages of the script
stages:
  - Analyze Script
  - Deploy to Production

pylint:
  stage: Analyze Script
  allow_failure: true
  script:
  - pylint script.py
  
production:
  stage: Deploy to Production
  script:
  - python script.py
```