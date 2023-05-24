s = 'step7_noPBC_'
def fileList(r1, r2):
  
    if (r1 == r2):
        return r1
  
    else:
        res = []
        while(r1 < r2+1 ):
              
            res.append("%s%s" % (s,r1))
            r1 += 1
        return res
loop= True 
while loop:
    r1 = input("Type the number of your first trajectory: ")
    r1 = int(r1)
    r2 = input("Type the number of your last trajectory: ")
    r2 = int(r2)
    if (r1 or r2)%2 == 1 or (r1 or r2)%2 == 0:
        f = open('file_input.txt','w')
        for i in fileList(r1,r2):
            f.write(i + '.xtc ')
        f.close()
        loop=False
    else: print('%f is not a valid number'%(n))

t2 = r2-r1
def timeList(t1, t2):
  
    if (t1 == t2):
        return r1
  
    else:
        res = []
        while(t1 < t2+1 ):
              
            res.append(t1*1000)
            t1 += 1
        return res
loop= True 
while loop:
    t1 = input("Type the start, in nanoseconds, of your first trajectory (default is 0): ")
    t1 = int(t1)
    if t1 == 0:
        f = open('time_input.txt','w')
        for i in timeList(t1,t2):
            f.write(str(i)+'\n')
        f.close()
        loop=False
    else: print('This script is not designed for starting times other than 0 ns')
