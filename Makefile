build:
	docker-compose up --build -d

clean:
	docker-compose down
	docker system prune -fa
	docker volume prune -f

deploy:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up --build -d