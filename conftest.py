import configparser
import os
import definitions

# pytest_plugins = "pytest-allure-adaptor"
# pytest_plugins = "allure.pytest_plugin"s

config = configparser.ConfigParser()

curPath = os.getcwd()  #获取当前路径

configFile = definitions.ROOT_DIR+'\config.ini'

config.read(configFile)

env = config['common']['env']
dataPath = config['common']['dataPath']

webHost = config[env]['webHost']
signHost = config[env]['signHost']
apiHost = config[env]['apiHost']
apiKey = config[env]['apiKey']
entryPassageID = config[env]['entryPassageID']
exitPassageID = config[env]['exitPassageID']
