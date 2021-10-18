import re
import os
#
pathDir = os.path.abspath('./')
# 文件夹路径
baseDir = os.path.dirname(pathDir)
# 文件路径
baseFile = os.path.basename(pathDir)
# listDir = os.listdir(pathDir)
print(baseDir)
print(baseFile)
# print(listDir)
# print(os.path.getsize(pathDir))
# total = 0
# for file in os.listdir(pathDir):
#     total = total + os.path.getsize(os.path.join("E:\\workspaces\\quickPython\\regularexpressions", file))
# print(total)
# dirExists = os.path.exists("E:\\workspaces\\quickPython")
# print(dirExists)
# with open('fileTest.txt', 'r', encoding='utf8') as f:
#     # read()：将文件内容读取为字符串
#     file = f.read()
#     print(file)
# with open('fileTest.txt', 'r', encoding='utf8') as f:
#     # readlines()：将文件内容读取为字符串列表
#     file = f.readlines()
#     print(file)
# import shelve
#
# # 变量写入mydata.txt文件
# shelveData = shelve.open('mydata.txt')
# cats = ['Zophie', 'Pooka', 'Simon']
# shelveData['cats'] = cats
# shelveData.close()
#
# # 读取变量
# shelveData = shelve.open('mydata.txt')
# print(type(shelveData))
# print(shelveData['cats'])
# #
# import pprint
# cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
# # pprint.pformat():返回一个字符串，可以写入文件
# pFile = pprint.pformat(cats)
# print(pFile)
# # 写入文件
# with open("myCats.py", "w") as f:
#     f.write('cats = ' + pprint.pformat(cats) + '\n')
#
# # 获取变量
# from regularexpressions import myCats
# name = myCats.cats[0]['name']
# # print(name)
# try:
#     for file in os.listdir("."):
#         if re.search('test.*?.py', file) is None:
#             print('该文件不是test开头')
#         else:
#             print(re.search('^test.*?.py', file).group())
# except Exception as e:
#     raise e
# import shutil
#
# # shutil 模块：
# # shutil.copy(source, destination)，将路径source 处的文件复制到路径destination处的文件夹
# dirC = shutil.copy('./test01.py', '../fileTest/test001.py')
# print(dirC)
# # 调用 shutil.move(source, destination)，将路径 source 处的文件夹移动到路径destination，并返回新位置的绝对路径的字符串。
# # shutil.move('./app1.apk', '../fileTest/app2.app')
# # destination 路径也可以指定一个文件名,代表移动并重命名
# shutil.move('./fileTest.txt', '../fileTest/filemove.txt')
# # 构成目的地的文件夹必须已经存在，否则 Python 会抛出异常
# shutil.move('./myCats.py', '../test')
# for file in os.listdir('../fileTest'):
#     if file.endswith('.txt'):
#         os.unlink(file)
#
#
# import send2trash
# # 利用 send2trash它会将文件夹和文件发送到计算机的垃圾箱或回收站，而不是永久删除它们
# send2trash.send2trash('../fileTest/app2.app')
# # 遍历文件树
# '''
# os.walk()函数被传入一个字符串值，即一个文件夹的路径。你可以在一个 for
# 循环语句中使用 os.walk()函数，遍历目录树os.walk()在循环的每次迭代中，返回 3 个值:
# 1．当前文件夹名称的字符串。
# 2．当前文件夹中子文件夹的字符串的列表。
# 3．当前文件夹中文件的字符串的列表。
# '''
# for folderName, subfolders, filenames in os.walk('../'):
#     print('当前文件夹： ' + folderName)
#     for subfolder in subfolders:
#         print('当前子文件夹 ' + folderName + ': ' + subfolder)
#     for filename in filenames:
#         print('文件名 ' + folderName + ': ' + filename)
#     print('')
#
# '''
# ZipFile 对象有一个 namelist()方法，返回 ZIP 文件中包含的所有文件和文件夹
# 的字符串的列表。这些字符串可以传递给 ZipFile 对象的 getinfo()方法，返回一个关
# 于特定文件的 ZipInfo 对象。ZipInfo 对象有自己的属性，诸如表示字节数的 file_size
# 和 compress_size，它们分别表示原来文件大小和压缩后文件大小。ZipFile 对象表示
# 整个归档文件，而 ZipInfo 对象则保存该归档文件中每个文件的有用信息。
# '''
# import zipfile
#
# fileList = zipfile.ZipFile('../fileTest/Tms_Interface.zip')
# # namelist()方法，返回 ZIP 文件中包含的所有文件和文件夹的字符串的列表
# print(fileList.namelist())
#
# spamInfo = fileList.getinfo('.idea/inspectionProfiles/profiles_settings.xml')
#
# # 原来文件大小
# fileSize = spamInfo.file_size
# # 压缩后文件大小
# zipSize = spamInfo.compress_size
#
# # round() 方法返回浮点数x的四舍五入值。
# print("Compressed file is %sx smaller!" % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
#
# # ZipFile 对象的 extractall()方法从 ZIP 文件中解压缩所有文件和文件夹，放到当前工作目录中
# fileList.extractall('../fileTest/')
#
# # ZipFile 对象的 extract()方法从 ZIP 文件中解压缩单个文件,传递给 extract()的字符串，必须匹配 namelist()返回的字符串列表中的一个
# fileList.extract('tool/')
#
# # 创建和添加到 ZIP 文件
# createZip = zipfile.ZipFile('../fileTest/Tms_Interface.zip', 'w')
# createZip.write('../fileTest/test001.py', compress_type=zipfile.ZIP_DEFLATED)
# createZip.close()
