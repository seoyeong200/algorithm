# raw = input().replace("::", ":0:0:").split(":")
raw = input().split(":")
print(raw)

ipv6 = ['' for _ in range(8)]

flag=0; idx=0
for ip in raw:
    if len(ip) == 4: # 압축안된 문자는 그대로
        ipv6[idx] = ip; idx+=1
    elif len(ip) > 0: # 1~3자리 숫자 0 padding
        ipv6[idx] = "0"*(4-len(ip)) + ip; idx+=1
    else: # '' 일 때
        if flag == 0: # 0으로만 이루어진 그룹 ::로 바꾼 경우
            for _ in range(8-len(raw)+1):
                ipv6[idx] = "0000"; idx+=1
            flag = 1
        else: # flag 1, 그룹 ::로 압축하는 방법 이미 사용
            ipv6[idx] = "0000"; idx+=1



print(":".join(ipv6))


