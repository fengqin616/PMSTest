import configparser
import os
import sys

# pytest_plugins = "pytest-allure-adaptor"
# pytest_plugins = "allure.pytest_plugin"s

config = configparser.ConfigParser()

curPath = os.getcwd()  #获取当前路径
#
# curPath = os.path.split(os.environ['VIRTUAL_ENV'])[0]
# curPath = os.path.dirname(os.path.dirname(__file__))
# curPath = os.path.dirname(sys.modules['__main__'].__file__)
curPath = os.path.dirname(os.path.abspath(__file__))
print(curPath)
