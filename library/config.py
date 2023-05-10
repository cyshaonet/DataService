# -*- coding: utf-8 -*- 
# @Date:    2022/11/8

import os

PROJECT_NAME = 'DataService'
project_path = os.path.abspath(os.path.dirname(__file__))
if project_path.find('\\') != -1:
    separator = '\\'
else:
    separator = '/'
PROJECT_ROOT = project_path[:project_path.find(f"{PROJECT_NAME}") + len(f"{PROJECT_NAME}{separator}")]


def set_env(conf, project):
    if project == "A":
        back_path = "/AData/ABackupData/"
    elif project == "B":
        back_path = "/BData/BBackupData/"
    else:
        back_path = "/CData/CBackupData/"
    if conf == "pro":
        app_url = "https://pro.com"
    elif conf == "stg":
        app_url = "https://stg.com"
    elif conf == "test":
        app_url = "https://test.com"
    else:
        return exit("环境只有 test/stg/pro")
    return app_url, back_path
