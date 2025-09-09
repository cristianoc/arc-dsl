.PHONY: typecheck

typecheck:
	mypy --hide-error-context --no-color-output dsl.py solvers.py

.PHONY: submission

submission:
	$(MAKE) -C golf submission
