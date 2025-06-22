sudo apt update && sudo apt upgrade -y

sudo apt install docker.io docker-compose -y
sudo usermod -aG docker $USER
newgrp docker

docker-compose run airflow-webserver airflow db init

docker-compose up --build -d
