from ..example import *
from ..child import *
from ..child.child_second_example import child_example2
from ..class_child import richet_object

import unittest
import os


# TestCase를 작성
class CustomTests(unittest.TestCase): 

    def test_runs(self):
        """단순 실행여부 판별하는 테스트 메소드"""
        hello_requests()

    def test_parent_using_child_module(self):
        """parent가 child의 함수만 import한 상황에 이걸 쓰는 경우."""
        child_example.child_example_time()

    def test_child_package(self):
        """child패키지에서만 import한 패키지를 사용하는 코드"""
        child_example.child_example_time()

    def test_second_child_package(self):
        """child패키지에서만 import한 모듈을 쓰는 함수만 import했을 때"""
        child_example2()

    def test_class_child(self):
        a = richet_object.RichetObject("testing example")
        a.print_name()

# unittest를 실행
if __name__ == '__main__':  
    unittest.main()