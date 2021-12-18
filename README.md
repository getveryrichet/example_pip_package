# example_pip_package


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
