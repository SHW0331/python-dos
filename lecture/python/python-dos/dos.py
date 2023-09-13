import socket
import threading
import random
import string

# options 설정
target_host = '192.168.209.128'
target_port = 8080
target_path = ''
size = 0
iterations = 50000

# # 더미 데이터 생성 함수
# def generate_dummy_data(size):
#     characters = string.ascii_letters + string.digits
#     return ''.join(random.choice(characters) for _ in range(size))

# request msg 수정
def modify_get_request(path, host) :
        request = f'GET /{path} HTTP/1.1\r\n' # start line
        request += f'Host: {host}\r\n' # headers
        request += f'\r\n' # body
        return request

# # 출발지 ip binding
# def source_ip_binding():
#     binding_ip = f'192.168.{random.randint(0, 255)}.{random.randint(0, 255)}'
#     return binding_ip

# 스레드에서 실행할 함수
def connect_to_server(thread_id, iterations):
    for i in range(iterations):
    
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.settimeout(1)
        msg = modify_get_request(target_path, target_host)
        # src_ip = source_ip_binding()
        # data = generate_dummy_data(1000)

        try:
            # client.bind((src_ip, 8080))
            client.connect((target_host, target_port))
            client.send(msg.encode('utf-8'))
            print(f'Thread {thread_id}: 연결 성공 - {i}')
        except socket.error as e:
            print(f'Thread {thread_id}: 연결 실패 - {e}')
        finally:
            client.close()

# 스레드 생성 및 시작
num_threads = 4  # 원하는 스레드 수
threads = []

for thread_id in range(num_threads):
    thread = threading.Thread(target=connect_to_server, args=(thread_id, iterations))
    threads.append(thread)
    thread.start()

# 모든 스레드가 종료될 때까지 대기
for thread in threads:
    thread.join()

print("모든 스레드가 종료되었습니다.")
