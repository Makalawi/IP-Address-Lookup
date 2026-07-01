import socket

website = input("Website: ")

ip = socket.gethostbyname(website)

print("IP Address:", ip)