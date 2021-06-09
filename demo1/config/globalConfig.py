#coding=UTF-8
import os
from public.utils.iniConfigParser import ReadConfigIni


# get path of ini file
ini_file_path = os.path.split(os.path.realpath(__file__))[0]
# get ini file
readConfig = ReadConfigIni(os.path.join(ini_file_path,"config.ini"))
# get absolute path of this project
project_path = readConfig.getConfigValue("project","project_path")
# get testcase's path
testCase_path = os.path.join(project_path,"testCase")
# get path of test report
testReport = os.path.join(project_path,"report")
# get path of test data
testData_path = os.path.join(project_path,"Data","testData")



if __name__ == "__main__":
    print(testCase_path)