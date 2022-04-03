# WIP -> Automatically establish VPN connection if connected to specific AP

import NetworkManager
import time
import dbus.mainloop.glib
import subprocess

OpenVPN_connected = False
pid_OpenVPN = 0
pid_Tunnel = 0

def main():
    print("[*] Initialising..")

    #Dbus setup
    print("[*] Establishing D-Bus connection!")
    dbus.mainloop.glib.DBusGMainLoop(set_as_default=True)
    print("[*] Connected!")

    #Get wifi name
    while(True):
        ActiveWifi = getWifiName()
        print("[*] Wifi is:", ActiveWifi)
        if(ActiveWifi == "XXXXXXXX"):
            print("[*] Connected to TFO-BZ Wifi!")
            ConnectOpenVPN()
            print("[*] Connected!")

        else:
            print("[*] Wifi is not XXXXXXXXXX Wifi!")

            print("[*] Is VPN running?")
            if(OpenVPN_connected):
                killOpenVPN()
                print("[*] Killing OpenVPN!")

        print("[*] Hibernating..")
        time.sleep(300)

def ConnectOpenVPN():
    OpenVPN_connected = True

    child = 



def killOpenVPN():
    OpenVPN_connected = False
    
    



def getWifiName():
    print("[*] Checking connected wifi...")
    ActiveConnections = []
    active = [x.Connection for x in NetworkManager.NetworkManager.ActiveConnections]
    for connection in NetworkManager.Settings.Connections:
        if connection in active:
            ActiveConnections.append(connection.GetSettings()['connection']['id'])

    return ActiveConnections[0]

if __name__ == "__main__":
    main()
