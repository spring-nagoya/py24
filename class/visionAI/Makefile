build:
	docker-compose build

creaet-network:
	docker network create py-default

bash:
	docker-compose run --rm python-develop-environment bash

run: build
	docker-compose run --rm python-develop-environment python main.py
	

.PHONE: build create-network bash run 