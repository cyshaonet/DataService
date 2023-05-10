# -*- coding: utf-8 -*- 
# @Date:    2022/11/8
# 24小时动态血压

from library.config import PROJECT_ROOT
import shutil
import time


class OptXml:
    def __init__(self, barcode, username, project, install_path, back_path):
        self.now = time.strftime("%Y-%m-%d %H:%M:%S").format(time.localtime())
        self.date = time.strftime("%Y-%m-%d").format(time.localtime())
        self.date_time = time.strftime("%Y%m%d").format(time.localtime())
        self.barcode = barcode
        self.username = username
        self.project = project
        self.path = install_path
        self.back_path = back_path

    def create_xml(self):
        filename = self.barcode + "_" + self.username + "_" + self.date
        xml = filename + ".xml"
        pdf = filename + ".pdf"
        if self.project == "C":
            result_path = "abpm_iresult"
        else:
            result_path = "abpm_result"
        with open(f"{PROJECT_ROOT}/data/abpm/demo.xml", "r", encoding="utf-8") as f:
            content = f.read().format(username=self.username, barcode=self.barcode, date_time=self.date)
        with open(f"{self.path}/{result_path}/{xml}", "w+", encoding="utf-8") as f1:
            f1.write(content)
            print(f"生成文件：{xml}")
        if shutil.copy(f"{PROJECT_ROOT}/data/abpm/demo.pdf", f"{self.path}/{result_path}/{pdf}"):
            print(f"生成文件：{pdf}")
        print("24小时动态血压 上传中...")
        time.sleep(6)
        try:
            with open(f"{self.path}{self.back_path}{self.date_time}/{result_path}/{xml}", "r"):
                return "24小时动态血压 上传文件成功，请查验数据解析"
        except:
            return f"24小时动态血压 上传文件失败，请检查！"
