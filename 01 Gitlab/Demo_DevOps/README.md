# IP Address Getter

This project will print the IP address of a website using the in-built `socket` library into a Pandas dataframe.

## Prerequisites

### Docker  
Docker is a set of Platform as a Service (PaaS) products that uses OS-level virtualization to deliver software in packages called containers. Containers are isolated from one another and bundle their own software, libraries and configuration files; they can communicate with each other through well-defined channels.

Install Docker Desktop for Windows by following the instructions on the official Docker website.

https://docs.docker.com/docker-for-windows/

### Gitlab Runner  
GitLab Runner is the open source project that is used to run your jobs and send the results back to GitLab. It is used in conjunction with GitLab CI/CD, the open-source continuous integration service included with GitLab that coordinates the jobs.

For the project, we will be installing our Gitlab Runner inside a Docker container.

- Create a New Folder on your Desktop
- Inside this folder create a file named `docker-compose.yml` using VS Code
- Copy paste the following inside the `docker-compose.yml` file
```
version: "3"

services:
  gitlab-runner:
    image: gitlab/gitlab-runner:alpine-v11.2.0
    container_name: gitlab_runner
    restart: always
    volumes:
      - ./config/:/etc/gitlab-runner/
      - /var/run/docker.sock:/var/run/docker.sock
```
- Create another file in the same folder named `register_runner.bat`

```
docker-compose run --rm gitlab-runner register -n^
 --url <url>^
 --registration-token <registration-token>^
 --executor docker^
 --description "DevOps Demo Gitlab Runner"^
 --docker-image "docker:stable"^
 --docker-volumes /var/run/docker.sock:/var/run/docker.sock

echo Gitlab Runner Image created

docker-compose up -d

echo Gitlab Runner Server started
```
- Go to the repo on Gitlab that you want to run your Gitlab CI/CD pipeline on. In our case, that will be the current repository `https://naopsgit.exu.ericsson.se/supply/sandbox/demo_gitlab`
- On the vertical Menubar on the left, select `Settings > CI / CD`
- On the section named `Runners` click on the `Expand` button
- In the column named `Specific Runners` and the section named `Set up a specific Runner manually`, copy the highlighted URL for the Gitlab website
- In the newly created `register_runner.bat` file, replace the `<url>` string with the Gitlab website
- Follow the same previous steps and replace the `<registration-token>` string with the Registration token
- Run the `register_runner.bat` file to now run the Gitlab Runner inside a Docker container
- To check if the Gitlab Runner has been registered, go to the `Runners` section of the Gitlab repo and check for newly installed Runners under `Specific Runners` column

## Running the project

- Create another New Folder on your Desktop
- Open the folder and type in `cmd` in the address bar to open up Command Prompt from that specific folder
- Copy-paste the following command to clone this repository
```
git clone https://naopsgit.exu.ericsson.se/supply/sandbox/demo_gitlab/
```
- Navigate to the folder for the repo by typing in `cd demo_gitlab` in the same Command Prompt.
- Open up the `script.py` file and in the dictionary variable named `data` add a url for a website, for example `www.youtube.com`