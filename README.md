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
這邊提供兩種方法，建議使用第一種
將下面超連結的`YourMoodleURL`改成你學校的Moodle網址 `ex:moodle.ntust.edu.tw`  
`YourUsername`改成你的Moodle username  
`YourPassword`改成你的Moodle password  

##### 1. 

第一種方法根據作業系統有一點差異  

###### Windows  

打開cmd(命令提示字元)  
輸入如下
```
curl "https://YourMoodleURL/login/token.php?service=moodle_mobile_app" -d "username=YourUsername&password=YourPassword"
```

###### Linux  

打開terminal
輸入如下
```
curl -X POST -d 'username=YourUsername&password=YourPassword' https://YourMoodleURL/login/token.php?service=moodle_mobile_app
```

###### Mac
打開terminal
輸入如下
```
curl -X POST -d 'username=YourUsername&password=YourPassword' https://YourMoodleURL/login/token.php?service=moodle_mobile_app
```

##### 2.

<https://YourMoodleURL/login/token.php?username=YourUsername&password=YourPassword&service=moodle_mobile_app>

在瀏覽器送出會拿到屬於你的`MOODLE_TOKEN` 先記下來等等會用到

如果你的密碼有特殊字元導致你拿不到token  
請到 https://www.urldecoder.org/ 把你的特殊字元做decode  
再把你decode的結果替換掉密碼中原本的特殊字元 如`#`換成`%23`

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

### Docker

如果您有使用Docker的話，可以試著將MoodleNotify架設在Docker上，以下指令請在終端機操作。

#### 架設MoodleNotify

##### 1. 首先請自行下載此專案
```bash
git clone https://github.com/MirrorShih/MoodleNotify.git
```

##### 2. 打開Dockerfile，將上述提到的環境變數填入到第15~18行中對應的位置，接著把`#`註解去掉，更改完的結果會是下面的樣子
```dockerfile
# Environment Variables
ENV MOODLE_TOEKN=(Your MOODLE_TOKEN)
ENV LINE_TOKEN=(Your LINE_TOKEN)
ENV MOODLE_URL=(Your MOODLE_URL)
ENV NOTIFY_TIME=(Your NOTIFY_TIME)
```

##### 3. 修改完Dockerfile之後，輸入以下指令建立映像檔
```bash
sudo docker build -t moodle_notify:latest .
```

##### 4. 完成映像檔之後建立容器執行
```bash
sudo docker run -d --name moodle_notify moodle_notify:latest
```

這樣就大功告成了。

#### 移除MoodleNotify

若您需要將MoodleNotify移除，則請輸入以下指令將容器以及映像檔移除
```bash
sudo docker rm -f moodle_notify
sudo docker rmi moodle_notify
```
