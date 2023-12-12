build:
	docker-compose build

creaet-network:
	docker network create py-default

bash:
	docker-compose run --rm py-dev-environment bash

run:
	docker-compose run --rm py-dev-environment python main.py
	
.PHONE: build create-network bash run