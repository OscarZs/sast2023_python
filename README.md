# sast2023 word game

## basic部分

### 环境配置

目前没有第三方依赖项，可以直接用 Python 运行。

### 使用设置

约定以下参数：

```{.bash}
--file / -f  接文章的路径
--namme / -n  接文章的标题
```

文章使用 JSON 存储，的格式如下：

```{.json}
{
  "articles": [
    {
      "title": "文章 1",
      "content": "这是一个关于{{1}}的{{2}}。",
      "hints": ["形容词", "名词"],
      "words": ["有趣的", "编程"]
    },
    {
      "title": "文章 2",
      "content": "另一个关于{{1}}的{{2}}。",
      "hints": ["形容词", "名词"],
      "words": ["迷人的", "技术"]
    }
  ]
}
```

### 游戏功能

1. 游戏从提供的文件(如所提供的articles.json)中读取文章。
2. 如果命令行参数中提供了特定的文章标题，游戏会选择该文章。否则，它会随机选择一篇文章。
3. 游戏显示所选文章的标题和内容。
4. 游戏根据提供的提示，提示用户输入缺失的单词。
5. 游戏用用户输入的单词替换文章中的缺失单词。
6. 游戏显示最终带有用户答案的文章。
7. 最后，游戏显示正确答案。

要开始游戏，请运行以下命令：

```{.bash}
python word_game.py --file <path_to_article_file>
```

如果您没有提供 --name 参数，游戏将从提供的文件中随机选择一篇文章。

玩得愉快！

## advanced部分

利用了streamlit库，可以在网页上进行游戏。
同时利用了try-except语句，可以在用户输入错误时提示用户重新输入。
(事实上也并不advanced。)
显示上有点小Bug，但是不影响使用。
