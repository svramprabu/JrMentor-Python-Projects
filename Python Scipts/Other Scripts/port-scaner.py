#it4min
import socket
so=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("""
          channel: @LinuxArmy
          programmer : it4min
  
""")
TargetIP=input("Enter the ip >>> ")
StartPort=int(input("Start For Range Port >>> "))
EndPort=int(input("End For Range Port >>> "))
def scan(port):
    try:
        so.connect((TargetIP,port))
        return True
    except:
        return False
print("****** Scan Start *****\n")
for port in range(StartPort,EndPort+1):
    if scan(port):
        print("[+] Port : "+str(port)+" Open" )
    else:
        print("[-] Port : "+str(port)+" Close" )
print("\n****** Scan Finished *****")
input()