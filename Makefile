install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=hello --cov=greeting tests
	#python -m pytest --nbval notebook.ipynb	#tests our jupyter notebook
	#python -m pytest -v tests/test_web.py #if you just want to test web

debug:
	python -m pytest -vv --pdb # Degugger is invoked

format:
	black *.py

lint:
	pylint --disable=R,C *.py

all: install lint test format