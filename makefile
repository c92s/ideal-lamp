build:
	python -m build

run: build
	pip install dist/$(shell ls dist | grep .whl) --force-reinstall
	python examples/app.py