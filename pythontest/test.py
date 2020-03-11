n=0
i=[]
s=[]
check=0

with open('input.txt') as f:
    while True:
        line = f.readline()
        if not line: break
        line = line.rstrip('\r\n')
        if ":" in line:
            str=line.split(":")
            i.append(int(str[0]))
            s.append(str[1])
            n+=1
        else:
            num=int(line)
            
            
d=sorted(zip(i,s))
                                
                       
for k in range(n):
    if num % d[k][0] ==0:
        print(d[k][1],end="")
        check=1
                       
if check==0:
    print(num)   
