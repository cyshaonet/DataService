# -*- coding: utf-8 -*-
# @Date:    2022/11/24
# 肺功能J21

from library.config import PROJECT_ROOT
import shutil
import time


class OptCsv:
    def __init__(self, barcode, username, project, install_path, back_path):
        self.now = time.strftime("%Y-%m-%d %H:%M:%S").format(time.localtime())
        self.tnow = time.strftime("%Y-%m-%dT%H:%M:%S+08:00").format(time.localtime())
        self.date = time.strftime("%Y%m%d").format(time.localtime())
        self.date_hms = time.strftime("%H%M%S").format(time.localtime())
        self.barcode = barcode
        self.username = username
        self.project = project
        self.path = install_path
        self.back_path = back_path

    def create_csv(self):
        filename = self.username + "_" + self.barcode + "_ROCC_" + self.date + "_" + self.date_hms
        csv = filename + ".csv"
        pdf = filename + ".pdf"
        result_path = "lfx_result"

        with open(f"{PROJECT_ROOT}/data/lfx/demo.csv", "r", encoding="utf-8") as f:
            content = f.read().format(username=self.username, barcode=self.barcode, now=self.tnow)
        with open(f"{self.path}/{result_path}/{csv}", "w+", encoding="utf-8") as f1:
            f1.write(content)
            print(f"生成文件：{csv}")
        if shutil.copy(f"{PROJECT_ROOT}/data/lfx/demo.pdf", f"{self.path}/{result_path}/{pdf}"):
            print(f"生成文件：{pdf}")
        print("肺功能康讯 上传中...")
        time.sleep(6)
        try:
            with open(f"{self.path}{self.back_path}{self.date}/{result_path}/{csv}", "r"):
                return "肺功能康讯 上传文件成功，请查验数据解析"
        except:
            return f"肺功能康讯 上传文件失败，请检查！"
