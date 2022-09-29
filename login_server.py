import socket
import random

HOST = ''
PORT = 50007

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('서버가 시작되었습니다.')
    conn, addr = s.accept()
    with conn:
        print('클라이언트 접속. {}'.format(addr))
        while True:
            data = conn.recv(1024).decode('utf-8')
            print('데이터:{}'.format(data))
            