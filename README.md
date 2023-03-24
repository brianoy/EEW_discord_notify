# EEW_discord_notify
地震速報、速報軟件、discord webhook推播、discord webhook推送（配合地牛Wake Up!）
由於地牛wake up!只能觸發*cmd*和*bat*，如果想要推送到其他軟體就要call到python
![image](https://user-images.githubusercontent.com/24865458/227400276-f5e9f40e-3ebf-4a7e-bc0a-77aba39ba5c3.png)

# 使用說明


## 第一步 架設python環境(不示範)(請確保系統環境變數中有python路徑)

## 第二步 獲取discord伺服器內的頻道webhook網址(在想要的頻道中點擊右鍵編輯頻道)
<img src="https://user-images.githubusercontent.com/24865458/208754730-8b555ce3-bc43-447b-9c04-3a4f9f26b0e7.png" width="50%">

## 第三步 下載zip解壓縮在想要的路徑

## 第四步 在地牛wake up!中選擇剛剛解壓縮的earthquick.bat路徑
<img src="https://user-images.githubusercontent.com/24865458/208751019-a2ca4838-1839-4e55-9cf6-a49853e98d78.png" width="50%">

## 第五步 調整earthquick.bat中設定notify.py檔案的位置
<img src="https://user-images.githubusercontent.com/24865458/208752205-64f9032a-04c8-4af9-bfb2-abef3875c4b1.png" width="50%">

## 第六步 填入discord webhook的網址

```https://discord.com/api/webhooks/1000000000000000000/XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX```

<img src="https://user-images.githubusercontent.com/24865458/208753148-5973652d-1088-44f3-8878-334774366a3e.png" width="50%">


## 第七步 在地牛wake up!中點擊測試

<img src="https://user-images.githubusercontent.com/24865458/227400584-86fa5f4c-5f41-40d8-b1d0-a2ac437390a6.png" width="50%">

## 第八步 看看訊息有沒有跳出來

![image](https://user-images.githubusercontent.com/24865458/227400802-92ab6e7c-0834-46e6-b8be-6e906572b1ad.png)
