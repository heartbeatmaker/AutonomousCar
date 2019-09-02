'''클라이언트 소켓을 담당하는 서버 클래스'''

class client:

    def __init__(self, cs, ip):
        self.cs = cs
        self.ip = ip

    def send_msg(self, message):
        self.cs.send(message.encode('utf-8'))

