.PHONY: test
deps:
	pip install -r requirements.txt; \
	pip install -r test_requirements.txt

console_run:
	PYTHONPATH=. python3 src/consoleMain.py

server_run:
	PYTHONPATH=. python3 src/serverMain.py

lint:
	flake8 src test

test:
	PYTHONPATH=. py.test  --verbose -s

