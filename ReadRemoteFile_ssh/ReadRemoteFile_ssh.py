# -*- encoding: utf-8 -*-

import paramiko

host = '192.168.133.130'
user = 'jumborur'
secret = 'Kjrjvjnbd12345!'
port = 22

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=host, username=user, password=secret, port=port)

'''
sft_client = ssh_client.open_sftp()

f_remote = sft_client.open('test.txt')

for line in f_remote:
    print(line)
'''

stdin, stdout, stderr = ssh_client.exec_command('cat test.txt')

#print(stdout.read().decode(encoding='UTF-8'))
#print("==================\n")
while True:
    print(stdout.readline()) #If first operator "print" was launched than second "print" don't write nothing
#sft_client.close()

ssh_client.close()
