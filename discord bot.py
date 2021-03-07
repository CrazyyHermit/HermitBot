from mcstatus import MinecraftServer
import discord

ip = "Kulduniokas.aternos.me"
try:
    server = MinecraftServer.lookup(ip)
    try:
        latency = server.ping()
        print(f"Server {ip} is online")
    except:
        print("The server is offline")
except ValueError:
    print("Invalid adress")
