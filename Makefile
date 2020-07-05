create-env:
	@virtualenv --python='/usr/bin/python3' .venv

run_app:
	@python main.py