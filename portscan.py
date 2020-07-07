import threading
import socket
import sys
#ip = socket.gethostbyname(target)


def getTargets(ip, iprange):
    ips = []
    ipSeparated = []
    ipSeparated=ip.split(".")
    if iprange == 24:
        for i in range(0, 256):
            ips.append("%s.%s.%s.%s" % (ipSeparated[0], ipSeparated[1], ipSeparated[2], i))
    
    if iprange == 16:
        for i in range(0,256):
            for i2 in range(0, 256):
                ips.append("%s.%s.%s.%s" % (ipSeparated[0], ipSeparated[1], i, i2))


    if iprange == 8:
        print("This will take like 10 seconds cuz it needs to generate 16777216 ips")
        for i in range(0,256):    
            for i2 in range(0,256):
                for i3 in range(0, 256):
                    ips.append("%s.%s.%s.%s" % (ipSeparated[0], i, i2, i3))
    return ips

def portscan(port):
    target = getTargets(str(sys.argv[1]), int(sys.argv[2]))
    for targettedBoi in target:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        if len(sys.argv) == 4:
            s.settimeout(float(sys.argv[3]))
        s.settimeout(0.5) 

        try:
            con = s.connect((targettedBoi,port))
            print("->%s:%s" % (targettedBoi, port))

            con.close()
        except: 
            pass
r = 1 

if len(sys.argv) < 3:
        print("Usage: python script.py ip iprange(ex: 24, 16, 8) [OPTIONAL]timeout")
        exit()

for x in range(1,65535): 
    t = threading.Thread(target=portscan,kwargs={'port':r}) 

    r += 1     
    t.start() 
