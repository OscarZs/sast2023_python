import streamlit as st
from utils import *
import random

st.title("Welcome to the word filling game.")
try:
    file = st.text_input("Please input the file name(like articles.json):")
    with open(file, 'r', encoding="utf-8") as f:
        # 用 json 解析文件 f 里面的内容，存储到 data 中
        data = json.load(f)
        articles = data["articles"]
        name = st.text_input("Please input the title:")
        # 根据参数或随机从 articles 中选择一篇文章
        article = next((article for article in articles if article["title"] == name), None)
        if article:
            st.write("Here it is. Lst's play.")
        else:
            st.write("A random one for you to play.You can choose the title in the file")
            # 打印所有名字
            for article in articles:
                st.write(article["title"])
            article = random.choice(articles)
        # 给出合适的输出，提示用户输入
        st.write(article["title"])
        st.write(article["content"])
        # 获取用户输入并进行替换
        keys = get_inputs_advanced(article["hints"])
        # 给出结果
        st.write("Here is your answer:")
        st.write(replace(article["content"], keys))
        # 给出正确答案
        st.write("The correct answer is:")
        st.write(replace(article["content"], article["words"]))
except UnboundLocalError:
    st.error("The file does not exist")
except FileNotFoundError:
    st.error("The file does not exist")

