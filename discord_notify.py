import requests
import sys
dcUrl = "<discord webhook url>"

magnitude = str(sys.argv[1]).replace("+","強").replace("-","弱")
second = str(sys.argv[2])

def dcWebhook(payload)->None:
    data = {"content": str(payload)}
    requests.post(dcUrl, json=data)

msg = "警告：地區預計震度" + magnitude + "級地震\n預計到達時間:" + second + "秒"

dcWebhook(msg)


