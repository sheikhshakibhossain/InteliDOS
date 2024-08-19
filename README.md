# Intelligent_WiFi_DOS
When a WiFi faces DOS attack, it simply changes it's channel to avoid the automated attack. <br>
Here, I've solved the issue. It'll attack the Network. At the same time, it'll intelligently <br>
change it's own to match to the Victim's channel if the Access Point has changed it's channel. <br> <br>
It keeps track of BSSID of the Victim. So, If the Victim had changed it's Access Point's name,<br> 
it's no issue at all. It'll keep attacking on matter what.<br>



## Install Requirements:
```bash
sudo apt update
sudo apt install aircrack-ng -y
sudo apt install macchanger -y
```
