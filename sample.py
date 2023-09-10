# ----------------------------------------------------------
# サーバーへの接続情報を設定
IP_ADDRESS = '192.168.1.106'
USER_NAME = 'robot'
PASSWORD='maker'

# COMMAND
CMD = 'for f in /sys/class/tacho-motor/*; do echo $f; done'
# ----------------------------------------------------------
import paramiko

results = []
# sshクライアント生成
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# アドレス、ユーザー名、パスワードを渡しconnection生成
client.connect(IP_ADDRESS, username=USER_NAME
               ,password=PASSWORD, timeout=5.0
               ,allow_agent=False, port=22
               ,look_for_keys=False)

# コマンドの実行
stdin, stdout, stderr = client.exec_command(CMD)
# コマンド実行結果を配列に格納
cmd_result = ''
for line in stdout:
    cmd_result += line
    results.append(line.replace('\n', ''))


# 実行結果を出力
print(cmd_result + "\n")
print(results)

# Clean up elements
client.close()
del client, stdin, stdout, stderr 
