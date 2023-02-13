#数据驱动
import os
import yaml

def read_testcase_yaml(yaml_path):
    with open(os.getcwd()+yaml_path,encoding="utf_8",mode="r") as f:
        value=yaml.load(stream=f,loader=yaml.FullLoader)
        return value