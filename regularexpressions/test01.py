import re

# compile()创建regex对象
phone = 'My number is 415-555-4242.'
phoneNum = re.compile(r'\d{3}-\d{3}-\d{4}')
# Regex 对象的search()方法查找传入的字符串将返回一个 Match 对象。

mo = phoneNum.search(phone)  # <re.Match object; span=(13, 25), match='415-555-4242'>

# Match 对象有一个 group()方法，它返回被查找字符串中实际匹配的文本
groupRegex = mo.group()
print(groupRegex)  # 415-555-4242

# 利用括号分组
