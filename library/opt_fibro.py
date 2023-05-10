# -*- coding: utf-8 -*-
# @Date:    2022/11/24
# 肝脏瞬时弹性硬度检测

from library.config import PROJECT_ROOT
import shutil
import time


class OptFibroJson:
    def __init__(self, barcode, username, project, install_path, back_path):
        self.exam_date = time.strftime("%Y-%m-%d %H:%M:%S").format(time.localtime())
        self.now_num = time.strftime("%Y%m%d%H%M%S").format(time.localtime())
        self.barcode = barcode
        self.username = username
        self.project = project
        self.path = install_path
        self.back_path = back_path
        self.date = self.now_num[0:8]
        self.time = self.now_num[8:14]

    def create_json(self):
        filename = self.barcode + "_" + self.username + "_" + self.date + "_" + self.time
        json = filename + ".json"
        pdf = filename + ".pdf"
        result_path = "fibro_result"
        with open(f"{PROJECT_ROOT}/data/fibro/demo.json", "r", encoding="utf-8") as f:
            content = f.read().replace("{barcode}", self.barcode).replace("{exam_date}", self.exam_date)
            # print(content)
        with open(f"{self.path}/{result_path}/{json}", "w+", encoding="utf-8") as f1:
            f1.write(content)
            print(f"生成文件：{json}")
        if shutil.copy(f"{PROJECT_ROOT}/data/fibro/demo.pdf", f"{self.path}/{result_path}/{pdf}"):
            print(f"生成文件：{pdf}")
        print("肝脏瞬时弹性硬度检测 上传中...")
        time.sleep(6)
        try:
            with open(f"{self.path}{self.back_path}{self.date}/{result_path}/{json}", "r"):
                return "肝脏瞬时弹性硬度检测 上传文件成功，请查验数据解析"
        except:
            return f"肝脏瞬时弹性硬度检测 上传文件失败，请检查！"
