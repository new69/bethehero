test:
	poetry run pytest --cov=src --cov-branch --cov-report=html

mypy:
	@echo
	poetry run mypy .

lint: mypy
	@echo
	poetry run ruff .
	@echo
	poetry run blue --check --diff --color .
	@echo
	poetry run pip-audit

format:
	poetry run ruff --silent --exit-zero --fix .
	poetry run blue .
