.PHONY: install format lint test notebook clean

install:
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt

format:
	ruff format .

lint:
	ruff check .

test:
	pytest

notebook:
	jupyter lab

clean:
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".ruff_cache" -exec rm -rf {} +
	find . -type d -name ".ipynb_checkpoints" -exec rm -rf {} +
