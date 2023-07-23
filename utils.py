import argparse
import json
import streamlit as st

def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    ...

    :return: 参数
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )

    parser.add_argument("-f", "--file", help="题库文件", required=True)
    # 添加更多参数
    parser.add_argument("-n","--name",help="题库文件",required=True)
    args = parser.parse_args()
    return args


def read_articles(filename):
    """
    读取题库文件

    :param filename: 题库文件名

    :return: 一个字典，题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        # 用 json 解析文件 f 里面的内容，存储到 data 中
        data = json.load(f)
        st.success("Available file")
    return data

def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """
    keys = []
    for hint in hints:
        print(f"请输入{hint}：")
        # 读取一个用户输入并且存储到 keys 当中
        keys.append(input())
    return keys

def get_inputs_advanced(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """
    keys = []
    for hint in hints:
        # 读取一个用户输入并且存储到 keys 当中
        keys.append(st.text_input(f"请输入{hint}："))
    return keys

def replace(article, keys):
    """
    替换文章内容

    :param article: 文章内容
    :param keys: 用户输入的单词

    :return: 替换后的文章内容

    """
    for i in range(len(keys)):
        # 将 article 中的 {{i}} 替换为 keys[i](用 str.replace() 函数)
        article = article.replace("{{" + str(i + 1) + "}}", keys[i])
    return article