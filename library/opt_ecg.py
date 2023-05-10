# -*- coding: utf-8 -*- 
# @Date:    2022/11/8
# 心电图解析

from library.config import PROJECT_ROOT
import shutil
import time


class OptXml:
    def __init__(self, barcode, username, project, install_path, back_path):
        self.now = time.strftime("%Y-%m-%d %H:%M:%S").format(time.localtime())
        self.now_num = time.strftime("%Y%m%d%H%M%S").format(time.localtime())
        self.date = time.strftime("%Y%m%d").format(time.localtime())
        self.barcode = barcode
        self.username = username
        self.project = project
        self.path = install_path
        self.back_path = back_path

    def create_xml(self):
        filename = self.barcode + "_" + self.username + "-男-28-" + self.now_num
        xml = filename + ".xml"
        pdf = filename + ".pdf"
        if self.project == "A":
            result_path = "ecg_result"
        elif self.project == "B":
            result_path = "ecg_result"
        else:
            result_path = "ecg_iresult"
        with open(f"{PROJECT_ROOT}/data/ecg/demo.xml", "r", encoding="utf-8") as f:
            content = f.read().format(username=self.username, barcode=self.barcode, now=self.now, now_num=self.now_num)
        with open(f"{self.path}/{result_path}/{xml}", "w+", encoding="utf-8") as f1:
            f1.write(content)
            print(f"生成文件：{xml}")
        if shutil.copy(f"{PROJECT_ROOT}/data/ecg/demo.pdf", f"{self.path}/{result_path}/{pdf}"):
            print(f"生成文件：{pdf}")
        print("心电图 上传中...")
        time.sleep(6)
        try:
            with open(f"{self.path}{self.back_path}{self.date}/{result_path}/{xml}", "r"):
                return "心电图 上传文件成功，请查验数据解析"
        except:
            return f"心电图 上传文件失败，请检查！"
