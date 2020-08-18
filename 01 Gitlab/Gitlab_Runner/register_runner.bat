docker-compose run --rm gitlab-runner register -n^
 --url https://naopsgit.exu.ericsson.se/^
 --registration-token s6Fe1xDs6_3gZ79fxyEB^
 --executor docker^
 --description "DevOps Demo Gitlab Runner"^
 --docker-image "docker:stable"^
 --docker-volumes /var/run/docker.sock:/var/run/docker.sock

echo Gitlab Runner Image created

docker-compose up -d

echo Gitlab Runner Server started