.PHONY: typecheck

typecheck:
	mypy --hide-error-context --no-color-output solvers.py

