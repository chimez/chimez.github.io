"""
File: cut_file_json
Author: chimez
Email: chimez@163.com
Github: https://github.com/chimez
Description: python3 -i cut_file_json.py -i file.wiki 
"""

import json
import sys
import getopt
import os
import jieba  # 分词


def save_json(article_index):
    """保存到json文件"""
    index_json = json.dumps(article_index)
    with open('article_index.json', 'w') as fi:
        fi.writelines(index_json)


def create_new_index():
    """新建空白索引json"""
    word_index = {}  # "word":[fileint,fileint]
    file_index = {}  # "filename":int
    file_array = [] #[int]:"filename"
    article_index = {}
    article_index["word_index"] = word_index
    article_index["file_index"] = file_index
    article_index["file_array"] = file_array
    save_json(article_index)
    return article_index


def load_index():
    """加载已有索引json"""
    with open('article_index.json', 'r') as fi:
        lines = fi.readlines()
    index_json = ""
    for line in lines:
        index_json += line
    article_index = json.loads(index_json)
    return article_index


def add_new_file(article_index, filename):
    """添加新的文件索引到map"""
    word_index = article_index["word_index"]
    file_index = article_index["file_index"]
    file_array = article_index["file_array"]
    filename_save = filename.replace('./','/').replace('.wiki','.html')
    if file_index == {} and file_array == []:
        file_index[filename_save] = 0
        file_array.append(filename_save)
    elif filename_save not in file_index.keys():
        file_index[filename_save] = max(file_index.values()) + 1
        file_array.append(filename_save)

    f_str = ""
    with open(filename, 'r') as fi:
        for line in fi.readlines():
            f_str += line

    for tk in jieba.tokenize(f_str):
        if tk[0] not in word_index.keys():
            word_index[tk[0]] = [file_index[filename_save]]
        elif file_index[filename_save] not in word_index[tk[0]]:
            word_index[tk[0]].append(file_index[filename_save])

    return article_index


def main(addfile):
    """加载已有的,添加新的,再保存"""
    article_index = load_index()
    add_new_file(article_index, addfile)
    save_json(article_index)


def add_all():
    for root, dirs, files in os.walk('.'):
        for name in files:
            filename = os.path.join(root, name)
            if "public_html" in filename \
                or "json" in filename  \
                or "diary" in filename:
                continue
            else:
                print(filename)
                main(filename)


try:
    # Short option syntax: "hv:"
    # Long option syntax: "help" or "verbose="
    opts, args = getopt.getopt(sys.argv[1:], "hvia:", ["help", "input", "all", "new"])

except getopt.GetoptError:
    # Print debug info
    print("!")

for option, argument in opts:
    if option in ("-h", "--help"):
        print("""
创建分词索引
-i filename --input filename    添加一个文件到索引
-a          --all               遍历当前文件夹所有文件并添加索引
-n          --new               创建新的空索引json""")
        sys.exit()

    elif option in ("-v", "--verbose"):
        verbose = argument

    elif option in ("-i", "--input"):
        main(argument)

    elif option in ("-a", "--all"):
        add_all()
    elif option == "--new":
        create_new_index()
