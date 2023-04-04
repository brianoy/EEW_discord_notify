import requests #網路
import time #睡眠
import sys #輸入引數
from os.path import exists #檔案存在
import configparser #config檔案管理

config = configparser.ConfigParser()

dcUrl = "https://discord.com/api/webhooks/1000000000000000000/abcdefghijklmnopqrstuvwxyz_ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789000000" #default url
sleep_time = "5"
area = "NULL"

def check_and_get()->None:
    global dcUrl,sleep_time,area
    if not exists("./discord_notify.ini"):
        print("webhook設定檔遺失，已重新創建新檔案")
        config['DEFAULT']['1.網址說明'] = "請複製discord webhook網址進去，無須加雙引號"
        config['DEFAULT']['webhookurl'] = dcUrl
        config['DEFAULT']['2.延遲說明'] = "請輸入在程式結束後視窗保留的時間，預設為5秒鐘，無須加雙引號"
        config['DEFAULT']['sleep_time'] = sleep_time
        config['DEFAULT']['3.地區說明'] = "請輸入在地震訊息發出後，需要被顯示的地區，預設不顯示，為NULL，無須加雙引號"
        config['DEFAULT']['area'] = area
        with open('discord_notify.ini', 'w') as file_path:#卻需要這個寫入..
            config.write(file_path)
    else:
        #with open('discord_notify.conf', 'r') as file_path: #不作動
        config.read("./discord_notify.ini")
        dcUrl = str(config["DEFAULT"]["webhookurl"])
        sleep_time = str(config["DEFAULT"]["sleep_time"])
        area = str(config["DEFAULT"]["area"])

def msg()->str:
    global dcUrl,sleep_time,area
    try:
        magnitude = str(sys.argv[1]).replace("+","強").replace("-","弱")
        second = str(sys.argv[2])
        #magnitude = str(2) #testnum
        #second = str(500) #testnum
        if str(area) == "NULL":
            msg = "警告：地區預計震度" + magnitude + "級地震\n預計到達時間:" + second + "秒"
        else :
            msg = "警告：" + str(area) + "地區預計震度" + magnitude + "級地震\n預計到達時間:" + second + "秒"
        return msg

    except IndexError as e:
        print("未輸入引數錯誤，ERROR:"+str(e))
        print("可能是由於使用者直接點擊本程式所導致")
        print("請參考github內步驟說明")
        print("試著透過地牛wakeup!中的測試按鈕才能傳入引數來做測試")
        return "Error:未收到傳入引數"
    
def sleep()->None:
    global sleep_time
    for i in range(int(sleep_time),0,-1):
        time.sleep(1)
        print(str(i) + "秒後關閉視窗")

def dcWebhook(dcUrl,payload)->None:
    data = {"content": str(payload)}
    do_post = requests.post(dcUrl, json=data)
    #print(do_post)
    if do_post.status_code != 204:
        print("傳送網址：" + str(dcUrl) + "\n傳送資料：" + str(data))
        print("在傳送webhook時發生錯誤，可能是由於輸入錯誤的webhook網址")
    
if __name__ == "__main__":
    check_and_get()
    dcWebhook(dcUrl=dcUrl, payload=msg())
    sleep()


