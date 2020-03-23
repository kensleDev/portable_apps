#encoding=utf8
import os
import subprocess
import platform
from wox import Wox,WoxAPI

class Hosts(Wox):

    def query(self,s):
        proxies = {}
        if self.proxy and self.proxy.get("enabled") and self.proxy.get("server"):
            proxies = {
              "http": "http://{}:{}".format(self.proxy.get("server"),self.proxy.get("port")),
              "http": "https://{}:{}".format(self.proxy.get("server"),self.proxy.get("port"))
            }
            #self.debug(proxies)

        results = []
        
        results.append({"Title": 'Open hosts file' ,"IcoPath":"Images/hosts.png","JsonRPCAction":{"method": "openHosts","dontHideAfterAction":True}})
        with open(r'C:\Windows\System32\drivers\etc\hosts', 'r') as f:
            for line in f:
                if '#' == line[0] or len(line)<2:
                    continue
                if s in line:
                    results.append({"Title": line ,"IcoPath":"Images/hosts.png","JsonRPCAction":{"method": "openHosts","dontHideAfterAction":False}})
        return results

    def openHosts(self):
        if 'AMD64' == platform.machine():
            subprocess.call(os.path.dirname(os.path.abspath(__file__)) + '\elevate_x64.exe notepad.exe C:\Windows\System32\drivers\etc\hosts')
        else:
            subprocess.call(os.path.dirname(os.path.abspath(__file__)) + '\elevate_x86.exe notepad.exe C:\Windows\System32\drivers\etc\hosts')
if __name__ == "__main__":
    Hosts()
