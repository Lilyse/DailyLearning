import urllib.request
import urllib.parse
import json

content = input("请输入翻译的内容：")


url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
data = {}
data['i'] = content
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = 'fanyideskweb'
data['salt'] = '1523019934074'
data['sign'] = 'a72a0b94d5223ace5549d266b166c819'
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CLICKBUTTION'
data['typoResult'] = 'false'
data = urllib.parse.urlencode(data).encode("utf-8")

     
response2 = urllib.request.urlopen(url,data)
html = response2.read().decode("utf-8")
target = json.loads(html)
print("翻译成： %s" % target["translateResult"][0][0]['tgt'])
