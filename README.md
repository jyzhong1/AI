# 将图片中的中文、英文识别为文字，生成可编辑的文本。供学习用。

1、先决条件:安装好PyQt5，opencv-python，Pillow和pytesseract。
pip install PyQt5 opencv-python Pillow pytesseract

2、运行:
python wordRecognize.py

3、通过ctrl+v复制图片到本软件，点击菜单识别，右侧为识别后的文本。

4、软件思路：
1）根据训练大数据集，训练出机器学习识别算法模型。
2）对于图片数据，识别出文本，显示在编辑区。
3）支持对识别的文本编辑、保存。
