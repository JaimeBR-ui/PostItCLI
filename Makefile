# Jaime Bohorquez

make:
	python3 setup.py sdist bdist_wheel

clean:
	@rm -r dist
	@rm -r build
	@rm -r postIt_JaimeBR_ui.egg-info
