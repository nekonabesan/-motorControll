import paramiko
import time

class connectEv3Dev():
    IP_ADDRESS = '192.168.1.106'
    USER_NAME = 'robot'
    PASSWORD='maker'

    client=None

    def __init__(self):
        # sshクライアント生成
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # アドレス、ユーザー名、パスワードを渡しconnection生成
        self.client.connect(self.IP_ADDRESS, username=self.USER_NAME
                    ,password=self.PASSWORD, timeout=5.0
                    ,allow_agent=False, port=22
                    ,look_for_keys=False)
        
    def sendForList(self, command: str):
        time_sta = time.time()
        results = []
        # コマンドの実行
        stdin, stdout, stderr = self.client.exec_command(command)
        # コマンド実行結果を配列に格納
        for line in stdout:
            line = line.replace('\n', '')
            #ディレクトリパス 「/sys/class/tacho-motor/」の最後の要素を戻り値に設定
            list = line.split('/')
            results.append(list.pop())
        del stdin, stdout, stderr
        time_end = time.time()
        tim = time_end- time_sta
        print(tim)
        return results
    
    def sendForSet(self, command: str):
        time_sta = time.time()
        # コマンドの実行
        stdin, stdout, stderr = self.client.exec_command(command)
        # コマンド実行結果をに格納
        del stdin, stdout, stderr
        time_end = time.time()
        tim = time_end- time_sta
        print(tim)
        return True
    
    def sendForGet(self, command: str):
        time_sta = time.time()
        # コマンドの実行
        stdin, stdout, stderr = self.client.exec_command(command)
        result = 0
        for line in stdout:
            result = line
        # コマンド実行結果をに格納
        del stdin, stdout, stderr
        time_end = time.time()
        tim = time_end- time_sta
        print(tim)
        return result
    
    def sendForSensorsList(self, command: str):    
        time_sta = time.time()
        results = []
        # コマンドの実行
        stdin, stdout, stderr = self.client.exec_command(command)
        # コマンド実行結果を配列に格納
        for line in stdout:
            line = line.replace('\n', '')
            #ディレクトリパス 「/sys/class/lego-sensor/」の最後の要素を戻り値に設定
            list = line.split('/')
            results.append(list.pop())
        del stdin, stdout, stderr
        time_end = time.time()
        tim = time_end- time_sta
        print(tim)
        return results

    def __del__(self):
        del self.client