# example_pip_package

## How to install
with https
```
pip install git+https://github.com/getveryrichet/example_pip_package.git
```
with ssh
```
pip install git+ssh://git@github.com/getveryrichet/example_pip_package.git
# or
pip install git+ssh://git@github.com-personal/getveryrichet/example_pip_package.git
```


If you install, then you should be able to use example package.

__init__.py represents .py files are used as pacakage and name of .py file will be the name of the package.
Therefore, since you have example.py in example directory, if you want to use example, then you should import as shown below
```python
from example import example
example.hello_requests()
```

if you want to use child_example.py, then
```python
from example.child import child_example
child_example.child_example()
```

if you want import all .py modules with command `from {directory} import *`,
then you should write `__all__ = ["{package name}"]` in __init__.py file as written in `example/__init__.py` file

## Test Cases
check this link below to learn how to set testcases using ùnittest` package
https://docs.python.org/3/library/unittest.html

In python 3, if you're using unittest.TestCase, You must have an empty (or otherwise) __init__.py file in your test directory (must be named test/)
You should have __init__.py to find parent package's relative path
Your test files inside test/ match the pattern test_*.py. They can be inside a subdirectory under test/, and those subdirs can be named as anything.

Then, you can run all the tests with in root directory:
```
python -m unittest
```
Done! A solution less than 100 lines. Hopefully another python beginner saves time by finding this.

## setup.py
`setup()` takes several arguments. This example package uses a relatively minimal set:

- `name` is the *distribution name* of your package. This can be any name as long as it only contains letters, numbers, `_` , and ``. It also must not already be taken on pypi.org. **Be sure to update this with your username,** as this ensures you won’t try to upload a package with the same name as one which already exists.
- `version` is the package version. See **[PEP 440](https://www.python.org/dev/peps/pep-0440)** for more details on versions.
- `author` and `author_email` are used to identify the author of the package.
- `description` is a short, one-sentence summary of the package.
- `long_description` is a detailed description of the package. This is shown on the package detail page on the Python Package Index. In this case, the long description is loaded from `README.md`, which is a common pattern.
- `long_description_content_type` tells the index what type of markup is used for the long description. In this case, it’s Markdown.
- `url` is the URL for the homepage of the project. For many projects, this will just be a link to GitHub, GitLab, Bitbucket, or similar code hosting service.
- `project_urls` lets you list any number of extra links to show on PyPI. Generally this could be to documentation, issue trackers, etc.
- `classifiers` gives the index and [pip](https://packaging.python.org/en/latest/key_projects/#pip) some additional metadata about your package. In this case, the package is only compatible with Python 3, is licensed under the MIT license, and is OS-independent. You should always include at least which version(s) of Python your package works on, which license your package is available under, and which operating systems your package will work on. For a complete list of classifiers, see [https://pypi.org/classifiers/](https://pypi.org/classifiers/).
- `package_dir` is a dictionary with package names for keys and directories for values. An empty package name represents the “root package” — the directory in the project that contains all Python source files for the package — so in this case the `src` directory is designated the root package.
- `packages` is a list of all Python [import packages](https://packaging.python.org/en/latest/glossary/#term-Import-Package) that should be included in the [distribution package](https://packaging.python.org/en/latest/glossary/#term-Distribution-Package). Instead of listing each package manually, we can use `find_packages()` to automatically discover all packages and subpackages under `package_dir`. In this case, the list of packages will be `example_package` as that’s the only package present.
- `python_requires` gives the versions of Python supported by your project. Installers like [pip](https://packaging.python.org/en/latest/key_projects/#pip) will look back though older versions of packages until it finds one that has a matching Python version.