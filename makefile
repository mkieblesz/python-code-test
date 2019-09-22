clean: ## clean run files
	find . -type d -name __pycache__ | xargs rm -rf

fix-permissions: ## fix permissions for all files which has been created inside container
	sudo chown -R $(USER):$(USER) .

check-for-updates: ## check if there are any new required pip package releases
	pip-check

migrate: ## run unapplied migrations
	python manage.py migrate

load-fixtures: ## load initial data useful for getting around when starting
	python manage.py shell < fixtures/users.py
	python manage.py shell < fixtures/starships.py
	# python manage.py import_starships

format: ## autoformat python files
	black -S -l 100 --exclude migrations shiptrader testsite fixtures

lint: ## lint python files
	flake8

test: lint ## run tests
	python manage.py test

exec: ## exec into docker container
	docker-compose exec code-test sh

build: ## build starship marketplace api image
	docker-compose build code-test

run: build ## build and run api with required services
	docker-compose up -d

	# wait for postgres server to be ready
	@until docker-compose exec --user postgres postgresql pg_isready | \
		grep -qm 1 "accepting connections"; do sleep 1; echo "Waiting for postgres" ; done
	@echo "Postgres accepting connections"

	# migrate and load initial data
	docker-compose exec code-test make migrate load-fixtures

kill: ## shutdown all services
	docker-compose kill && docker-compose rm --force
	docker-compose down

help:
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
