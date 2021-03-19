.PHONY: env lint

env:
	python3.6 -m venv env
	env/bin/pip install -r requirements.txt

lint:
	env/bin/flake8
