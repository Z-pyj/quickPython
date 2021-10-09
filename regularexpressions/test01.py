import re

#
# # compile()创建regex对象
# phone = 'My number is 415-555-4242.'
# phoneNum = re.compile(r'\d{3}-\d{3}-\d{4}')
# # Regex 对象的search()方法查找传入的字符串将返回一个 Match 对象。
# # 包含被查找字符串中的“第一次”匹配的文本
# mo1 = phoneNum.search(phone)  # <re.Match object; span=(13, 25), match='415-555-4242'>
#
# # Match 对象有一个 group()方法，它返回被查找字符串中实际匹配的文本
# groupRegex = mo1.group()
# print(groupRegex)  # 415-555-4242
#
# # 利用括号分组
# phoneNumGroup = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
# mo2 = phoneNumGroup.search(phone)
# # 向 group()匹配对象方法传入整数 1 或 2，就可以取得匹配文本的不同部分。向 group()方法传入 0 或不传入参数，将返回整个匹配的文本。
# print(mo2.group())
# print(mo2.group(1))
# print(mo2.group(2))
#
# # groups()方法一次性获取全部,因为 mo.groups()返回多个值的元组，所以你可以使用多重赋值的技巧
# num1, num2, num3 = mo2.groups()
# print(num2)
#
# # 字符|称为“管道”。希望匹配许多表达式中的一个时，就可以使用它，如果多个表达式都出现在被查找的字符串中，第一次出现的匹配文本，将作为 Match 对象返回
# heroRegex = re.compile(r'Batman|Tina Fey')
# mo3 = heroRegex.search('Tina Fey and Batman.')  # 第一次出现的匹配文本，将作为 Match 对象返回
# print(mo3.group())
#
# # 用问号实现可选匹配
# # 字符?表明它前面的分组在这个模式中是可选的
# batRegex = re.compile('Bat(wo)?man')
# mo4 = batRegex.search('The Adventures of Batman')
# print(mo4.group())
#
# # *意味着“匹配零次或多次”，即星号之前的分组，可以在文本中出现任意次。它可以完全不存在，或一次又一次地重复
# batRegexN1 = re.compile('Bat(wo)*man')
# mo5 = batRegexN1.search('The Adventures of Batwowowoman')
# print(mo5.group())
# # +（加号）则意味着“匹配一次或多次”
# batRegexN2 = re.compile('Bat(wo)+man')
# mo6 = batRegexN2.search('The Adventures of Batwoman')
# print(mo6.group())
#
# # 用花括号匹配特定次数
# batRegexN3 = re.compile('(Has){2,3}')
# mo6 = batRegexN3.search('HasHas,HasHasHas')
# print(mo6.group())

call = 'Cell: 415-555-9999 Work: 212-555-0000'
phoneNum = re.compile(r'\d{3}-\d{3}-\d{4}')
callAll = phoneNum.findall(call)  # ['415-555-9999', '212-555-0000']

# 如果正则表达式中有分组，那么findall将返回元组的列表。每个元组表示一个找到的匹配，其中的项就是正则表达式中每个分组的匹配字符串
phoneNumGroup = re.compile(r'(\d{3}-(\d{3})-(\d{4}))')
callAllGroup = phoneNumGroup.findall(call)  # [('415-555-9999', '555', '9999'), ('212-555-0000', '555', '0000')]

print(callAllGroup)
# 通配符
# 通过传入 re.DOTALL 作为 re.compile()的第二个参数，可以让句点字符匹配所有字符，包括换行字符
# 要让正则表达式不区分大小写，可以向 re.compile()传入 re.IGNORECASE 或 re.I，作为第二个参数。

name = 'Agent Alice gave the secret documents to Agent Bob.'
agentName = re.compile('^Agent \w+')
newName = agentName.sub('替换name', name)  # 替换name gave the secret documents to Agent Bob.
print(newName)
import os

str1 = os.path.join('usr', 'bin', 'spam')  # usr\bin\spam
print(str1)

# 获取当前路径
str2 = os.getcwd()
print(str2)
# # 修改当前工作路径
# str3 = os.chdir(r'E:\workspaces\quickPython')
# print(str3)