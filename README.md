# RSA_Project

# Running the project

./run.sh

Create a docker network

sudo docker network create vanetzalan0 --subnet 192.168.98.0/24
sudo docker-compose build
sudo docker-compose up 

list networks:

sudo docker-network ls

remove network:

sudo docker network rm vanetzalan0


list containers:

sudo docker container ps -a


stop containers:

sudo docker container stop CONTAINER


delete containers:

sudo docker container prune