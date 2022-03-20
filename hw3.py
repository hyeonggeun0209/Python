from sys import stdin
print("20181494 지형근")
print("비트열을 입력하시오.")
code = stdin.readline().strip()
print("입력된 비트열:" + code)
fcs = [0] * 3
for i in range(len(code)) : 
    num = int(code[i]) ^ fcs[0]
    fcs[0] = num ^ fcs[1]
    fcs[1] = fcs[2]
    fcs[2] = num
    print("".join(map(str,fcs)))
print("FCS: " + "".join(map(str,fcs)))