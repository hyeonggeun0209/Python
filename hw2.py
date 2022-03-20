from sys import stdin
print("20181494 지형근")
print("해밍코드를 입력하시오.")
code = list(map(int,stdin.readline().strip()))
print("입력된 해밍코드: " + "".join(map(str,code)))
p,count,parity,res= 1, 0, 0, 0
for i in range(len(code)) :
    if i+1 == p :
        count += 1
        p *= 2
for j in range(count) :
    p = int(2**j)
    for i in range(p-1,len(code),p*2) :
        for k in range(p) :
            if i+k > len(code)-1 :
                break
            parity ^= code[i+k]
    if parity == 1 :
        res += p
        parity = 0

if res > 0 :
    code[res-1] ^= 1
    print(str(res) + "번째 비트열에 에러 발생. 수정된 코드: "+ "".join(map(str,code))) 
else :
    print("에러없음")  

