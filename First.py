import re 
text = "today is 01/04/2015, happy new year..."
#建立日期的正则表达式 
detepat = re.compile('(\d+)/(\d+)/(\d+)')
#进行匹配并打印结果 
result = detepat.finditer(text) 
for m in result: 
  print(m.group()) 