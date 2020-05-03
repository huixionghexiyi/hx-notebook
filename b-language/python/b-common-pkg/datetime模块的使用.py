from  datetime import datetime
now =datetime.now() # 返回当前时间
print('当前时间：')
print(now)
dt = datetime(1995,12,6,12,20) # 创建一个指定时间的datetime对象
print('指定时间')
print(now)
ts = now.timestamp()# 浮点数表示时间戳，小数点后表示毫秒数，没有时区的概念
print('当前时间->时间戳：')
print(ts) 
fts = datetime.fromtimestamp(ts) # 将时间戳转换为本地时区的时间
print('时间戳->本地时区的时间：')
print(fts)
ufts = datetime.utcfromtimestamp(ts)# 时间戳转换utc标准时间
print('时间戳->指定时区的时间：')
print(ufts)
spt = datetime.strptime('2019-12-6 12:14:59','%Y-%m-%d %H:%M:%S') # str转datetime对象，第二个参数为时间格式
print('str转datetime:')
print(type(spt))
print(spt)
sft = now.strftime('%a, %b %d %H:%M') # datetime转str
print('datetime 转 str:')
print(sft)
from datetime import datetime,timedelta
now = datetime.now()
now = now + timedelta(hours=1)
print('时间增加一个小时：')
print(now)
from datetime import datetime,timedelta,timezone
tz_utc_8 = timezone(timedelta(hours=8))# 创建时区 UTC + 8：00
now = datetime.now()
print('指定时区：')
print(now)

# 时区转换  https://www.liaoxuefeng.com/wiki/1016959663602400/1017648783851616