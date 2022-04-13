x="""All that doth flow we cannot liquid name

Or else would fire and water be the same;

But that is liquid which is moist and wet

Fire that property can never get.

Then 'tis not cold that doth the fire put out

But 'tis the wet that makes it die, no doubt."""
print(len(x)) #len函数得到字符串长度
print(x.find('the')) #find检测字符串中是否包含"the"
print(x.rfind("the")) #rfind返回"the"最后一次出现的位置
print(x.count('the')) #count用于统计字符串里"the"出现的次数
print(x.isalpha()) # isalpha检测字符串是否只由字母或文字组成
print(x.isdigit()) #isdigit检测字符串是否只由数字组成