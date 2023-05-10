# -*- coding: utf-8 -*-
# @Date:    2022/11/24
# 肺功能J21

from library.config import PROJECT_ROOT
import shutil
import time


class OptCsv:
    def __init__(self, barcode, username, project, install_path, back_path):
        self.now = time.strftime("%Y-%m-%d %H:%M:%S").format(time.localtime())
        self.date = time.strftime("%Y%m%d").format(time.localtime())
        self.date_hms = time.strftime("%H%M%S").format(time.localtime())
        self.barcode = barcode
        self.username = username
        self.project = project
        self.path = install_path
        self.back_path = back_path

    def create_csv(self):
        filename = self.barcode + "_" + self.username + "_Data_" + self.date + "_" + self.date_hms
        csv = filename + ".csv"
        png = filename + ".png"
        result_path = "J21_result"

        with open(f"{PROJECT_ROOT}/data/J21/demo.csv", "r", encoding="utf-8") as f:
            content = f.read().format(username=self.username, barcode=self.barcode, date=self.date)
        with open(f"{self.path}/{result_path}/{csv}", "w+", encoding="utf-8") as f1:
            f1.write(content)
            print(f"生成文件：{csv}")
        if shutil.copy(f"{PROJECT_ROOT}/data/J21/demo.png", f"{self.path}/{result_path}/{png}"):
            print(f"生成文件：{png}")
        print("肺功能J21 上传中...")
        time.sleep(6)
        try:
            with open(f"{self.path}{self.back_path}{self.date}/{result_path}/{csv}", "r"):
                return "肺功能J21 上传文件成功，请查验数据解析"
        except:
            return f"肺功能J21 上传文件失败，请检查！"
