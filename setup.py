import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()
with open("requirements.txt", "r", encoding="utf-8") as r:
	requirements = r.read()

setuptools.setup(
	name='example',
	version='0.0.6',
	description='richet pip install test',
	long_description=long_description,
	long_description_content_type="text/markdown",
	url='https://github.com/getveryrichet/example_pip_package.git',
	author='richet',
	author_email='getveryrichet.oh@gmail.com',
	license='MIT',
	# packages=['example'],
	packages_dir={"":"example"},
	packages=setuptools.find_packages(),
	zip_safe=False,
	python_requires=">=3.6",
	install_requires=requirements

)