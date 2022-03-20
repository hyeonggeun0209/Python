from sys import stdin
print("20181494 지형근")
print("해밍코드로 변환시킬 데이터를 입력하시오.")
code = list(map(int,stdin.readline().strip()))
print("입력된 데이터: " + "".join(map(str,code)))
len_parity, i = 1, 0
k = 0
while(2**len_parity <= len(code)+len_parity+1) :
    len_parity += 1

data_code = [0] * (len(code)+len_parity+1)
for j in range(1, len(code)+len_parity+1) :
    if(j == 2**i) :
        data_code[j] = 0
        i+=1
    else :
        data_code[j] = code[k]
        k+=1
for j in range(1,len_parity+1) :
    p = int(2**(j-1))
    for i in range(p,len(data_code),p*2) :
        for k in range(p) :
            if i+k > len(data_code)-1 :
                break
            data_code[p] ^= data_code[i+k]
print("해밍코드: " + "".join(map(str,data_code[1::])))
