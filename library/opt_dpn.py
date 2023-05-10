# -*- coding: utf-8 -*- 
# @Date:    2022/11/8
# 旧版-神经传导

from library.config import PROJECT_ROOT
import time


class OptXml:
    def __init__(self, barcode, username, project, install_path, back_path):
        self.now = time.strftime("%Y-%m-%d %H:%M:%S").format(time.localtime())
        self.date = time.strftime("%Y%m%d%H%M%S").format(time.localtime())
        self.date_time = time.strftime("%Y%m%d").format(time.localtime())
        self.barcode = barcode
        self.username = username
        self.project = project
        self.path = install_path
        self.back_path = back_path

    def create_xml(self):
        filename = "dpncheckC14-00000000180907093230_" + self.date + "_ID" + self.barcode
        xml = filename + ".xml"
        if self.project == "A":
            result_path = "dpn_result"
        elif self.project == "B":
            result_path = "dpn_result"
        else:
            result_path = "dpn_iresult"
        with open(f"{PROJECT_ROOT}/data/dpn/demo.xml", "r", encoding="utf-16") as f:
            content = f.read().format(now=self.now, barcode=self.barcode, username=self.username)
        with open(f"{self.path}/{result_path}/{xml}", "w+", encoding="utf-16") as f1:
            f1.write(content)
            print(f"生成文件：{xml}")
        print("旧版DPN-神经传导 上传中...")
        time.sleep(6)
        try:
            with open(f"{self.path}{self.back_path}{self.date_time}/{result_path}/{xml}", "r"):
                return "旧版DPN-神经传导 上传文件成功，请查验数据解析"
        except:
            return f"旧版DPN-神经传导 上传文件失败，请检查！"
