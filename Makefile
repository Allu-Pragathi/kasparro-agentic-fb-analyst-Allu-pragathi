.PHONY: install run test

install:
	python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt

run:
	python src/orchestrator/run.py "Analyze ROAS drop in last 7 days"

test:
	pytest -q
