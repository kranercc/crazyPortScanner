import threading
import socket
import sys
import time
import os
#ip = socket.gethostbyname(target)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

ips = []
def getTargets(ip, iprange):
    global ips
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

    if iprange == 0:
        ips.append(ip)

nmapCommand = "nmap -sC -sV -oN nmap/fullScan -p"

portsOpenPerIP = []
def scan(ip, port):
#    print(enemyOfTheState[:15])
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if(len(sys.argv) > 3):
        s.settimeout(float(sys.argv[3]))

    s.settimeout(0.5)

    try:
        con = s.connect((ip,port))
        print(bcolors.OKGREEN + "[OPEN] -> %s:%s" % (ip, port) + bcolors.ENDC)
        portsOpenPerIP.append(port)

    
  
        con.close()
    except: 
        #print("Failed for %s on port %s" % (ip, port))
        pass


enemyOfTheState = ["0"]
def prepIpAndPorts():
    if(len(enemyOfTheState) < 2):
        getTargets(str(sys.argv[1]), int(sys.argv[2]))
        enemyOfTheState[0] = ips[0]
        for p in range(1,1000):
            enemyOfTheState.append(p)
        ips.pop(0)



def scanNetworks(port=""):
    try:
        if port != "":
            for ip in range(len(ips)):
                scan(ips[0], port)
                ips.pop(0)
        else:
            prepIpAndPorts()
            for i in range(1, len(enemyOfTheState)):
                scan(enemyOfTheState[0], enemyOfTheState[1])
                prepIpAndPorts()
                enemyOfTheState.pop(1)
    except:
        exit()


if len(sys.argv) < 3:
        print("Usage: python script.py ip iprange(ex: 24, 16, 8) [OPTIONAL]timeout(ex: 0.5) [OPTIONAL]port ")
        exit()

start = time.time()

getTargets(str(sys.argv[1]), int(sys.argv[2]))
for i in range(500):
    if(len(sys.argv) > 4):
        t = threading.Thread(target=scanNetworks, kwargs={'port':int(sys.argv[4])})
        t.start()
    else:
        t = threading.Thread(target=scanNetworks)
        t.start()



def checkMultiplePorts_antiloop():
    global portsOpenPerIP, nmapCommand, enemyOfTheState
    for port in portsOpenPerIP:
        if portsOpenPerIP.count(port) > 1:
            portsOpenPerIP.pop(-1)
            for p in portsOpenPerIP:
                if p != portsOpenPerIP[-1]:
                    nmapCommand += str(str(p) + ',')
                else:
                    nmapCommand += str(p)

            print("You may now use\n " +bcolors.OKGREEN+ "%s %s" % (nmapCommand,enemyOfTheState[0]) + bcolors.ENDC)
            
             
            os.kill(os.getpid(), 9)


old = 0

startTime = time.time()
while 1:
    checkMultiplePorts_antiloop()

    if (time.time() - startTime) > 5:
        if(len(sys.argv) < 5):
            old = len(enemyOfTheState)
            print(bcolors.OKBLUE +  "Enemy -> %s || The Most Recent Port Checked -> %s" % (enemyOfTheState[0], enemyOfTheState[1]) + bcolors.ENDC)

            print(bcolors.WARNING + "Ports scanned every 5 seconds: " + str(old - len(enemyOfTheState)) + bcolors.ENDC)
        
        startTime = time.time()
