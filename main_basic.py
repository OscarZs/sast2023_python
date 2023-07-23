from utils import *
import random

if __name__ == "__main__":
    print("Welcome to the word filling game.")
    args = parser_data()
    print(args.file)
    data = read_articles(args.file)
    articles = data["articles"]
    # 根据参数或随机从 articles 中选择一篇文章
    article = next((article for article in articles if article["title"] == args.name), None)
    if article:
        print("Here it is. Lst's play.")
    else:
        print("No article found. I choose a random one for you to play.")
        article = random.choice(articles)
    # 给出合适的输出，提示用户输入
    print(article["title"])
    print(article["content"])
    # 获取用户输入并进行替换
    keys = get_inputs(article["hints"])
    # 给出结果
    print("Here is your answer:")
    print(replace(article["content"], keys))
    # 给出正确答案
    print("The correct answer is:")
    print(replace(article["content"], article["words"]))
