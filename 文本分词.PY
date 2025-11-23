# encoding=utf-8
import jieba
import re
import os
import tkinter as tk
import Gemini_API_调用分词
from Gemini_API_调用分词 import ai_fenci
from tkinter import filedialog

OUTPUT_DIR = r'C:\Users\Camouf\Desktop\项目文件\数字人文个人作业'

file_path = filedialog.askopenfilenames(
    initialdir="C:\\Users\\Camouf\\Desktop\\项目文件\\数字人文个人作业", # 可以设置为您的初始目录
    title="请选择要加载的 TXT 文件",
    filetypes=[("文本文件", "*.txt")]
)
for i in file_path:
    new_path = OUTPUT_DIR + '\\' + '分词'+ os.path.basename(i)
    with open(i, 'r', encoding='utf-8') as f:
        file_content = f.read()

    seg_list = jieba.cut(file_content, cut_all=False)
    a = list(seg_list)
    print("Default Mode: " + " ".join(a))  # 精确模式
    with open(new_path, 'w', encoding='utf-8') as n:
        n.write(" ".join(a))

    # with open(new_path, 'w', encoding='utf-8') as n:
    #        n.write(ai_fenci(file_content))