#!/usr/bin/env python3
import scapy.all as scapy
import optparse

#getting user arguments
def get_arguments():
    parse = optparse.OptionParser()
    parse.add_option("-t", "--target", dest="ip", help="Target IP/ IP range")
    options = parse.parse_args()[0]
    return options #returing options

def scan(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    clients_list = []
    for element in answered_list:
        client_dict = {"IP": element[1].psrc, "MAC": element[1].hwsrc}
        clients_list.append(client_dict)
    return(clients_list)

def print_result(results_list):
    print("IP\t\t\tMAC Address\n---------------------------------------------------------")
    for client in results_list:
        print(client["IP"] + "\t\t" + client["MAC"])

options = get_arguments()
scan_result = scan(options.ip)
print_result(scan_result)
