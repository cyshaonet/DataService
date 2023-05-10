# -*- coding: utf-8 -*-
# @Date:    2022/11/8

from library import task
from pathlib import Path


def run(hj, proj, install):
    """
    执行的项目
    """
    if not Path(install).is_dir():
        exit("安装目录不存在")
    if proj == "A":
        task.A_run(hj, code, project, install)
    elif proj == "B":
        task.B_run(hj, code, project, install)
    elif proj == "C":
        task.C_run(hj, code, project, install)
    else:
        exit("项目只有 A/B/C")


if __name__ == '__main__':
    # 运行环境 test/stg/pro
    env = "stg"
    # 项目 A/B/C
    project = "A"
    # DataService Result路径
    data_service_path = "D:/AData/ADataResult/"
    # 患者Barcode
    code = "900000001"
    # 开始生成文件
    run(env, project, data_service_path)
