SERVICE_NAME=library
MY_DOCKER_NAME=$(SERVICE_NAME)
USERNAME=beata86
TAG=$(USERNAME)/$(MY_DOCKER_NAME)

.PHONY: test
deps:
	pip3 install -r requirements.txt; \
	pip3 install -r test_requirements.txt

console_run:
	PYTHONPATH=. python3 src/consoleMain.py

server_run:
	PYTHONPATH=. python3 src/serverMain.py

lint:
	flake8 src test

test:
	PYTHONPATH=. pytest --verbose -s test

docker_build:
	docker build -t $(MY_DOCKER_NAME) .

docker_run: docker_build
	docker run \
	   --name $(SERVICE_NAME)-dev \
	    -p 5000:5000 \
	    -d $(MY_DOCKER_NAME)

docker_run_remote:
	docker run \
	   --name $(SERVICE_NAME)-dev \
	    -p 5000:5000 \
	    -d $(USERNAME)/$(MY_DOCKER_NAME)

docker_stop:
	docker stop $(SERVICE_NAME)-dev || true

docker_clean: docker_stop
	docker rm $(SERVICE_NAME)-dev || true
	docker rmi $(MY_DOCKER_NAME) || true
	docker rmi $(USERNAME)/$(MY_DOCKER_NAME) || true

docker_push: docker_build
	@docker login --username $(USERNAME) --password $${DOCKER_PASSWORD}; \
	docker tag $(MY_DOCKER_NAME) $(TAG); \
	docker push $(TAG); \
	docker logout;