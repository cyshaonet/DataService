# -*- coding: utf-8 -*-
# @Date:    2022/11/8

from library.config import set_env
import requests
import json

from library import opt_ndi, opt_PC10, opt_3d
from library import opt_dpn
from library import opt_ecg
from library import opt_abpm
from library import opt_fmd
from library import opt_body
from library import opt_dexa
from library import opt_title_artery
from library import opt_big_artery
from library import opt_small_artery
from library import opt_vf
from library import opt_fibro
from library import opt_8900d
from library import opt_J21
from library import opt_lfx
from library import opt_tanita


def get_token(api_url):
    """
    获取医生登录信息
    """
    data = "grant_type=password&client_id=0&username=1&password=1"
    header = {"Content-Type": "application/x-www-form-urlencoded"}
    login_url = "{}/api/winAppAuth/v1/auth/login".format(api_url)
    res = requests.post(login_url, data=data, headers=header)
    if "success" in res.text:
        return "{} {}".format(res.json()["data"]["token_info"]["token_type"],
                              res.json()["data"]["token_info"]["access_token"]), \
            res.json()["data"]["user_id"]
    else:
        return exit(json.loads(res.text))


def get_name(barcode, access_token, api_url, doc_id):
    """
    获取患者信息
    """
    header = {
        "authorization": access_token
    }
    list_url = "{}/api/winAppAuth/v1/patient/getPatientInfo?parameters_json=".format(api_url)
    payload = {"access_token": None, "code": f"{barcode}", "code_type": "", "name": "", "sex": "", "cell": "",
               "bday": "", "doc_id": f"{doc_id}"}
    res = requests.post(list_url, headers=header, json=payload)
    if len(res.json()["data"]) == 0:
        return exit("无法找到对应的患者，请确认Barcode与环境匹配！")
    else:
        return res.json()["data"][0]["name"]


def A_run(env, barcode, project, install):
    """
    A生成解析文件
    """
    url = set_env(env, project)[0]
    doc_info = get_token(url)
    name = get_name(barcode, doc_info[0], url, doc_info[1])
    # 海神Ndi-神经传导
    print(opt_ndi.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 旧版DPN-神经传导
    print(opt_dpn.OptXml(barcode, name, project, install, set_env(env, project)[1]).create_xml())
    # 心电图
    print(opt_ecg.OptXml(barcode, name, project, install, set_env(env, project)[1]).create_xml())
    # 24小时动态血压
    print(opt_abpm.OptXml(barcode, name, project, install, set_env(env, project)[1]).create_xml())
    # 血管内皮
    print(opt_fmd.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 人体成分分析 - ma6000
    print(opt_body.OptCsv(barcode, name, project, install, set_env(env, project)[1], "ma6000").create_csv())
    # 人体成分分析 - ma8000
    print(opt_body.OptCsv(barcode, name, project, install, set_env(env, project)[1], "ma8000").create_csv())
    # 人体成分分析 - 百利达980
    print(opt_tanita.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_json())
    # 骨密度DEXA
    print(opt_dexa.OptJson(barcode, name, project, install, set_env(env, project)[1]).create_json())
    # 大动脉 - 带表头
    print(opt_title_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 大动脉 - 无表头
    print(opt_big_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 小动脉
    print(opt_small_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 内脏脂肪
    print(opt_vf.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())


def B_run(env, barcode, project, install):
    """
    B生成解析文件
    """
    url = set_env(env, project)[0]
    doc_info = get_token(url)
    name = get_name(barcode, doc_info[0], url, doc_info[1])
    # # 旧版DPN-神经传导
    # print(opt_dpn.OptXml(barcode, name, project, install, set_env(env, project)[1]).create_xml())
    # 心电图
    print(opt_ecg.OptXml(barcode, name, project, install, set_env(env, project)[1]).create_xml())
    # 24小时动态血压
    print(opt_abpm.OptXml(barcode, name, project, install, set_env(env, project)[1]).create_xml())
    # 血管内皮
    print(opt_fmd.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 大动脉 - 带表头
    print(opt_title_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 大动脉 - 无表头
    print(opt_big_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 小动脉
    print(opt_small_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 肝脏瞬时弹性硬度检测
    print(opt_fibro.OptFibroJson(barcode, name, project, install, set_env(env, project)[1]).create_json())
    # 内脏脂肪
    print(opt_vf.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 肺功能监测 - PC10
    print(opt_PC10.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 咳喘肺功能 - 康讯
    print(opt_lfx.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 咳喘肺功能 - 3d
    print(opt_3d.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 咳喘肺功能 - 8900d
    print(opt_8900d.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 咳喘肺功能 - J21
    print(opt_J21.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 人体成分分析 - ma6000
    print(opt_body.OptCsv(barcode, name, project, install, set_env(env, project)[1], "ma6000").create_csv())
    # 人体成分分析 - ma8000
    print(opt_body.OptCsv(barcode, name, project, install, set_env(env, project)[1], "ma8000").create_csv())
    # 人体成分分析 - 百利达980
    print(opt_tanita.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_json())


def C_run(env, barcode, project, install):
    """
    C生成解析文件
    """
    url = set_env(env, project)[0]
    doc_info = get_token(url)
    name = get_name(barcode, doc_info[0], url, doc_info[1])
    # 心电图
    print(opt_ecg.OptXml(barcode, name, project, install, set_env(env, project)[1]).create_xml())
    # 血管内皮
    print(opt_fmd.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 大动脉 - 带表头
    print(opt_title_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 大动脉 - 无表头
    print(opt_big_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
    # 小动脉
    print(opt_small_artery.OptCsv(barcode, name, project, install, set_env(env, project)[1]).create_csv())
