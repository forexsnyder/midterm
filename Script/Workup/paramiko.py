import paramiko
host = "192.168.1.38"
port = 22
username = "IEUser"
password = "admin123"

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(host, port, username, password)

stdin, stdout, stderr = ssh.exec_command('cd C:\User\IEUser\Downloads')
#lines = stdout.readlines()
#print(lines)

stdin, stdout, stderr = ssh.exec_command('ls')
lines = stdout.readlines()
print(lines)
