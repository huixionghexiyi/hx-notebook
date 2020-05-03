'''
这个库用于ssh登录和通过sftp协议的传输文件
'''
import paramiko
'''
# 通过SSH连接执行命令
'''
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.150.131',port=22,username='root',password='123456')

stdin,stdout,stderr = ssh.exec_command('ls /')

res,err = stdout.read(),stderr.read()
result = res if res else err
print(result.decode())
ssh.close()

import paramiko,os
'''
使用sftp协议完成文件传输
'''
transport = paramiko.Transport(('192.168.150.131',22))
transport.connect(username='root',password='123456')
sftp = paramiko.SFTPClient.from_transport(transport)
sftp.put(os.path.abspath(__file__),'/tmp/面试题.py')
sftp.get('/tmp/面试题.py',os.path.dirname(os.path.realpath(__file__))+'test.py')
transport.close()

import paramiko,os
'''
使用免密登录完成ssh连接，
核心思想就是，linux端有谁的公钥，谁就可以登录linux
所以可以在linux上创建ssh密钥，然后将私钥传到windows上，自己持有公钥
[测试后不能使用，问题未解决：2020年3月21日]
'''
private_key = paramiko.RSAKey.from_private_key_file(os.path.dirname(os.path.realpath(__file__))+'\id_rsa31.txt')#要将私钥放在这里
# 创建SSH对象
ssh = paramiko.SSHClient()
# 允许连接不在know_hosts文件中的主机
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接服务器
ssh.connect(hostname='10.0.0.41', port=22, username='fang', pkey=private_key)
# 执行命令
stdin, stdout, stderr = ssh.exec_command('df;ifconfig')
result = stdout.read()
print(result.decode())
stdin, stdout2, stderr = ssh.exec_command('ifconfig')
# 获取命令结果
result2 = stdout2.read()
print(result2.decode())
# 关闭连接
ssh.close()