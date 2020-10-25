clean:
	@rm -f *.db __pycache__

codecheck:
	@echo "Codestyle check backend"
	@flake8 backend
	@echo "Codestyle check frontend"
	@flake8 frontend

runtests:
	@echo "Unit test backend"
	@pytest backend/tests
	@echo "Unit test frontend"
	@pytest frontend/tests

runapp:
	@python main.py
