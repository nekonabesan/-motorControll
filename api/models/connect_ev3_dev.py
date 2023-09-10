import paramiko

class connectEv3Dev():
    IP_ADDRESS = '192.168.1.106'
    USER_NAME = 'robot'
    PASSWORD='maker'

    def send(self, command: str):
        results = []
        # sshクライアント生成
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # アドレス、ユーザー名、パスワードを渡しconnection生成
        client.connect(self.IP_ADDRESS, username=self.USER_NAME
                    ,password=self.PASSWORD, timeout=5.0
                    ,allow_agent=False, port=22
                    ,look_for_keys=False)

        # コマンドの実行
        stdin, stdout, stderr = client.exec_command(command)
        # コマンド実行結果を配列に格納
        for line in stdout:
            line = line.replace('\n', '')
            #ディレクトリパス 「/sys/class/tacho-motor/」の最後の要素を戻り値に設定
            list = line.split('/')
            results.append(list.pop())
        # Clean up elements
        client.close()
        del client, stdin, stdout, stderr 
        
        return results