import time
import platform
from datetime import datetime as dt

redirect="127.0.0.1"
website_list=["www.facebook.com","www.whatsapp.com"]
morningTime=dt(dt.now().year,dt.now().month,dt.now().day,8)
eveningTime=dt(dt.now().year,dt.now().month,dt.now().day,20)

def get_host_path():
    if platform.system().lower().strip()=="linux":
        return "/etc/hosts"
    if platform.system().lower().strip()=="windows":
        return r"C:\Windows\System32\drivers\etc\hosts"
    if platform.system().lower().strip()=="darwin":
        return "/etc/hosts"


def block_websites(host_path):
    while True:
        if dt.now()>morningTime and dt.now()<eveningTime:
                print("working hours")
                with open(host_path,"r+") as file:
                    content=file.read()
                    for website in website_list:
                        if website not in content:
                            file.write(redirect+" "+website+" \n")
                        else:
                            print("website already added")
                            pass
        else:
                print("free time")
                with open(host_path,"r+") as file:
                    content=file.readlines()
                    file.seek(0)
                    for line in content:
                        if not any(website in line for website in website_list):
                            file.write(line)
                    file.truncate()
        time.sleep(5)

host_path=get_host_path()
block_websites(host_path)
