# -*- coding: utf-8 -*- 
# @Date:    2022/11/8
# 骨密度DEXA

from library.config import PROJECT_ROOT
import shutil
import time


class OptJson:
    def __init__(self, barcode, username, project, install_path, back_path):
        self.now = time.strftime("%Y%m%d%H%M%S").format(time.localtime())
        self.date = time.strftime("%Y%m%d").format(time.localtime())
        self.barcode = barcode
        self.username = username
        self.project = project
        self.path = install_path
        self.back_path = back_path

    def create_json(self):
        filename = self.barcode + "_" + self.now + "_CheckResult_L"
        json = filename + ".json"
        pdf = filename + ".pdf"
        if self.project == "C":
            result_path = "dexa_iresult"
        else:
            result_path = "dexa_result"
        with open(f"{PROJECT_ROOT}/data/dexa/demo.json", "r", encoding="utf-8") as f:
            content = f.read().replace("{barcode}", self.barcode)
        with open(f"{self.path}/{result_path}/{json}", "w+", encoding="utf-8") as f1:
            f1.write(content)
            print(f"生成文件：{json}")
        if shutil.copy(f"{PROJECT_ROOT}/data/dexa/demo.pdf", f"{self.path}/{result_path}/{pdf}"):
            print(f"生成文件：{pdf}")
        print("骨密度DEXA 上传中...")
        time.sleep(6)
        try:
            with open(f"{self.path}{self.back_path}{self.date}/{result_path}/{json}", "r"):
                return "骨密度DEXA 上传文件成功，请查验数据解析"
        except:
            return f"骨密度DEXA 上传文件失败，请检查！"
