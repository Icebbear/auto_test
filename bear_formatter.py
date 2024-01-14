# -*-coding:utf-8 -*- #
# ---------------------------------------------------------------------------
# ProjectName:   i2share_requests
# FileName:      ice bear_formatter.py
# Author:       ice bear
# Datetime:     2024/1/11 23:13
# Description:
# 命名规范：文件名全小写+下划线，类名大驼峰，方法和变量小写+下划线连接，
# 常量大写，变量和常量用名词，方法用动词
# 该脚本作用为，遍历auto_test目录下所有的py文件，进行文本内字符串替换
# ---------------------------------------------------------------------------
import os


def get_file_paths(paths):
    """
    获取指定路径下所有的py文件，存入生成器内
    :param paths: 需要遍历的目录路径
    :return: 返回一个生产器，内容为指定目录内所有py文件的路径
    """
    paths = os.walk(top=paths, topdown=True)
    for path, dir_list, files_list in paths:
        for file_name in files_list:
            if file_name.endswith('.py'):
                file_path = os.path.join(path, file_name)
                yield file_path


def replace(file_path, old_str, new_str):
    """
    将文件内的字符串替换为新的字符串
    :param file_path:需要替换的文件全路径
    :param old_str: 需要替换的字符串
    :param new_str: 新的字符串
    :return: None
    """
    with open(file=file_path, mode='r', encoding='utf8') as f:
        content = f.read()

    content = content.replace(old_str, new_str)
    with open(file=file_path, mode='w', encoding='utf8') as f:
        f.write(content)


if __name__ == '__main__':
    # 获取当前py文件的路径，由此再获取auto_test目录的全路径
    format_path =os.path.dirname(__file__)
    # 循环从生成器中取出py文件的全路径，对这个文件进行字符串替换操作
    for path in get_file_paths(format_path):
        replace(path, "ice bear", "ice bear")
