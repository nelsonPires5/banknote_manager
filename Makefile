clean:
	@rm -rf *.db */__pycache__ __pycache__ */.pytest_cache .pytest_cache

codecheck:
	@flake8 backend frontend

runtests: clean
	@pytest backend/tests frontend/tests -vv

runapp:
	@python main.py
