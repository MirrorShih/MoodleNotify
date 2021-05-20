# MoodleNotify

定時用Line提醒你Moodle上文件更新的好幫手  
MoodleNotify會在每天下午4點(GMT+8)時提醒你過去24小時在moodle上被修改過的檔案以及目前可以參與的考試

## 使用教學

### 環境變數

有三個環境變數需要使用者進行設定
```
MOODLE_TOKEN
LINE_TOKEN
MOODLE_URL (台科學生不需設定)
```

#### MOODLE_TOKEN

將下面超連結的`YourMoodleURL`改成你學校的Moodle網址 `ex:moodle.ntust.edu.tw`  
`YourUsername`改成你的Moodle username  
`YourPassword`改成你的Moodle password

<https://YourMoodleURL/login/token.php?username=YourUsername&password=YourPassword&service=moodle_mobile_app>

在瀏覽器送出會拿到屬於你的`MOODLE_TOKEN` 先記下來等等會用到

#### LINE_TOKEN

點擊 [LINE Notify](https://notify-bot.line.me/my/) 在頁面最下方點擊`發行權杖`

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/Line_token.png)

權杖名稱填入`MoodleNotify` 選擇`透過1對1聊天接收LINE Notify的通知`並發行

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/Line_token_settings.png)

複製權杖先記下來 等等會用到

#### MOODLE_URL(台科學生不需設定)

學校所使用的Moodle網址 如<https://moodle.ntust.edu.tw/>(結尾一定要是`/`)

### Heroku

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

按下上方部署按鈕並跟隨以下步驟

#### 填入`app name`並按下`Deploy app`

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/heroku_deploy.png)

#### 等待`Deploy to Heroku`轉成綠色 按下`Manage App`

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/manage.png)

#### 進入管理頁面後按`Settings` 在設定頁面按`Reveal Config Vars`

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/config_vars.png)

#### 在這加入剛剛提到的環境變數

#### KEY填以下三個值

#### VALUE填相對應的TOKEN或URL

#### 如果是台科學生則可不填MOODLE_URL

```
MOODLE_TOKEN
LINE_TOKEN
MOODLE_URL
```

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/Vars.png)

#### 最後來到`Resources`把服務打開就可以了

![alt text](https://github.com/MirrorShih/MoodleNotify/blob/main/assets/resources.png)
