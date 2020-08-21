'''
다음의 결과와 같이 임의의 URL 주소를 입력받아 protocol, host,
나머지(path, querystring, ...)로 구분하는 프로그램을 작성하십시오.

입력
http://www.example.com/test?p=1&q=2

출력
protocol: http

host: www.example.com

others: test?p=1&q=2
'''
url = input()
idx = -1
colon_slesh1 = url.find('://')
colon_slesh1_len = colon_slesh1 + len('://')
colon_slesh2 = url.find('/', colon_slesh1_len)
colon_slesh2_len = colon_slesh2 + len('/')
while True:
    if idx == -1:
        print('protocol: {}'.format(url[0:colon_slesh1]))
        print('host: {}'.format(url[colon_slesh1_len:colon_slesh2]))
        print('others: {}'.format(url[colon_slesh2_len:]))
        idx = 0
    else:
        break





