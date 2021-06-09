import os
import configparser



"""
    解析ini文件
"""
class ReadConfigIni():

    """
        fileName:要解析的文件名
    """
    def __init__(self,fileName):
        self.parser = configparser.ConfigParser()
        self.parser.read(fileName)
    """
        config:配置项
        name:参数名
    """
    def getConfigValue(self,config,name):
        value = self.parser.get(config,name)
        return value