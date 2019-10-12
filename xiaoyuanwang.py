import urllib
import urllib.request
conf = {
'account': '1711013037@telecom',   #校园网账号
'passwd': '804547477',    #校园网秘密
'url': 'http://210.29.79.194/a79.htm'
}
form = {
'DDDDD': conf['account'],
'upass': conf['passwd'],
'0MKKey': '123456',
'v':''
}
data = urllib.parse.urlencode(form).encode("UTF8")
req = urllib.request.Request(conf['url'], data)
res = urllib.request.urlopen(req)

# python自己装，文件扔个启动项优先级高点的地方，比tim开的快就行
#   电信用户名后复制 @telecom
#   移动用户名后复制 @cmcc            不要加空格
#   联通用户名后复制 @unicom
#   校园网后不用加东西
