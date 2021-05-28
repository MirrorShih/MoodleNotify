# MoodleNotify

定時用Line提醒你Moodle上文件更新的好幫手  
MoodleNotify每天會定時提醒你moodle上的新資訊

#### 1.過去24小時内被修改過的檔案

#### 2.過去24小時内被修改過且現在還可以提交的作業

#### 3.過去24小時内開始且現在還可以作答的考試

## 使用教學

### 環境變數

有四個環境變數需要使用者進行設定
```
MOODLE_TOKEN
LINE_TOKEN
MOODLE_URL
NOTIFY_TIME
```

#### MOODLE_TOKEN

將下面超連結的`YourMoodleURL`改成你學校的Moodle網址 `ex:moodle.ntust.edu.tw`  
`YourUsername`改成你的Moodle username  
`YourPassword`改成你的Moodle password  
如果你的密碼有特殊字元導致你拿不到token  
請到 https://www.urldecoder.org/ 把你的特殊字元做decode  
再把你decode的結果替換掉密碼中原本的特殊字元 如`#`換成`%23`

<https://YourMoodleURL/login/token.php?username=YourUsername&password=YourPassword&service=moodle_mobile_app>

在瀏覽器送出會拿到屬於你的`MOODLE_TOKEN` 先記下來等等會用到

#### LINE_TOKEN

點擊 [LINE Notify](https://notify-bot.line.me/my/) 在頁面最下方點擊`發行權杖`

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/Line_token.png)

權杖名稱填入`MoodleNotify` 選擇`透過1對1聊天接收LINE Notify的通知`並發行

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/Line_token_settings.png)

複製權杖先記下來 等等會用到

#### MOODLE_URL

學校所使用的Moodle網址 如<https://moodle.ntust.edu.tw/>(結尾一定要是`/`)

#### NOTIFY_TIME

MoodleNotify提醒你的時間 為24小時制 設定16就是下午四點 8就是上午八點

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

按下上方部署按鈕並跟隨以下步驟

#### 填入`app name`和4個環境變數對應的值並按下`Deploy app`

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/heroku_deploy.png)

#### 等待`Deploy to Heroku`轉成綠色 按下`Manage App`

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/manage.png)

#### 最後來到`Resources`把服務打開就可以了

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/resources.png)
