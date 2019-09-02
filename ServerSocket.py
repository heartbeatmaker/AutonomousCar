import socket
import threading

'''
tcp 에코서버
'''

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('192.168.0.30', 8999))  # 서버 ip와 포트번호를 지정
server_socket.listen(0)  # 클라이언트의 연결요청을 기다리는 상태
print("Listening on 8999")


def thread():

    client_socket, addr = server_socket.accept()  # 연결요청을 받음
    print("connected client : ", addr[0], addr[1])
    t = threading.Thread(target=thread)
    t.start()

    while 1:
        data = client_socket.recv(65535)  # 클라이언트로부터 메시지를 수신받는다. 65535 ; 버퍼 사이즈
        client_socket.send(data)  # 클라이언트에게 받은 메시지를 그대로 돌려준다(echo)

        # 로그 남기기
        print("received data from client "+addr[0]+" : ", data.decode())

thread()