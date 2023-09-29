import time
import socket
import logging
import paramiko
import subprocess
#import api.service.connection.socket.client as client_socket_connection

class connectEv3Dev():
    IP_ADDRESS = '192.168.1.106'
    USER_NAME = 'robot'
    PASSWORD='maker'
    TARGET_PORT=50000

    client = None
    ev3_server_socket = None
    logger = None
    
    def __init__(self):
        # sshクライアント生成
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        # logging
        logging.basicConfig(format='%(levelname)s:%(asctime)s:%(pathname)s:%(lineno)s:%(message)s')
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG) 
        # アドレス、ユーザー名、パスワードを渡しconnection生成
        self.client.connect(self.IP_ADDRESS, username=self.USER_NAME
                    ,password=self.PASSWORD, timeout=5.0
                    ,allow_agent=False, port=22
                    ,look_for_keys=False)
        self.initSocket()
    
    def createSocketConnection(self):
        self.ev3_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.ev3_server_socket.connect((self.IP_ADDRESS, self.TARGET_PORT))
        self.ev3_server_socket.settimeout(2)

    def initSocket(self):
        try:
            if self.ev3_server_socket is None:
                self.createSocketConnection()
        except subprocess.CalledProcessError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            return False
        except ConnectionRefusedError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            return False
        except ConnectionError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            return False
        except Exception as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            return False

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
    
    def sendForValue(self, command: str):
        try:
            time_sta = time.time()
            # コマンドの実行
            stdin, stdout, stderr = self.client.exec_command(command)
            # コマンド実行結果を
            result = stdout.read()
            del stdin, stdout, stderr
            time_end = time.time()
            tim = time_end- time_sta
            print(tim)
            return result
        except Exception as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
    
    def sendForSet(self, command: str):
        try:
            time_sta = time.time()
            self.initSocket()
            # コマンドの実行
            print(command)
            self.ev3_server_socket.send(command.encode('utf-8'))
            result = self.ev3_server_socket.recv(4096)
            result = result.decode('utf-8')
            time_end = time.time()
            tim = time_end- time_sta
            print(tim)
            return result
        except ConnectionRefusedError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
        except BrokenPipeError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
        except Exception as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
    
    def sendForGet(self, command: str):
        try:
            time_sta = time.time()
            self.initSocket()
            # コマンドの実行
            print(command)
            self.ev3_server_socket.send(command.encode('utf-8'))
            result = self.ev3_server_socket.recv(4096)
            result = result.decode('utf-8')
            print('sendForGet : ' + result)
            print(result)
            time_end = time.time()
            tim = time_end- time_sta
            print(tim)
            return result
        except ConnectionRefusedError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
        except BrokenPipeError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
        except Exception as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
    
    def sendForSensorsList(self, command: str):
        try:
            time_sta = time.time()
            results = []
            self.initSocket()
            # コマンドの実行
            print(command)
            self.ev3_server_socket.send(command.encode('utf-8'))
            stdout = self.ev3_server_socket.recv(4096)
            stdout = stdout.decode('utf-8')
            # コマンド実行結果を配列に格納
            lines = stdout.split("\n")
            list = lines[0].split('/')
            results.append(list.pop())
            list = lines[1].split('/')
            results.append(list.pop())
            time_end = time.time()
            tim = time_end- time_sta
            print(tim)
            return results
        except ConnectionRefusedError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
        except BrokenPipeError as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False
        except Exception as e:
            #self.ev3_server_socket = None
            self.logger.debug(e.args, stacklevel = 2)
            self.createSocketConnection()
            return False

    def __del__(self):
        del self.client