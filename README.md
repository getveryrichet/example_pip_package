# example_pip_package

## How to install
```
pip install git+https://github.com/getveryrichet/example_pip_package.git
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
