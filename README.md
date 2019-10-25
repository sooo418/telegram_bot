![env](https://user-images.githubusercontent.com/50854729/67548540-06c2b480-f73d-11e9-8c70-ad994c0a74ae.PNG)

##### CHAT_ID에는 'https://api.telegram.org/bot자신의Telegram_Bot_Token/getUpdates'으로 접근하여 CHAT_ID값을 가져와서 입력해준다.



```
from decouple import config


token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
```

##### 해당 코드를 이용하여 .env파일에 저장된 "TELEGRAM_BOT_TOKEN"값과 "CHAT_ID"값을 token, chat_id에 넣어 사용할 수 있다.



## app.py 실행



### 메아리 기능

![메아리](https://user-images.githubusercontent.com/50854729/67488375-af740400-f6aa-11e9-82c1-599d69ce2141.PNG)

##### '/로또', '/vonvon'이 아닌 다른 말들은 똑같이 대답해준다.



### 로또기능

![로또](https://user-images.githubusercontent.com/50854729/67488376-af740400-f6aa-11e9-8e5e-36c77d27994b.PNG)

##### '/로또' 라고 입력하면 임의의 로또 번호를 제공해준다.



### 랜덤으로 포켓몬 정해주기

![포켓몬](https://user-images.githubusercontent.com/50854729/67488377-b00c9a80-f6aa-11e9-8ba6-6ac1bb9acd3f.PNG)

##### '/vonvon 이름'을 입력하면 임의로 받은 이름에 포켓몬을 정해준다.



## python anywhere를 활용하여 서버 배포하기

![pythonanywhereStart](https://user-images.githubusercontent.com/50854729/67488369-ae42d700-f6aa-11e9-93f9-f2c3a4ba262a.PNG)

##### https://www.pythonanywhere.com/로 가서 로그인 하여 상단에 Web으로 가서 화살표로 표시한 버튼을 클릭한다.



![pythonanywhereStart2](https://user-images.githubusercontent.com/50854729/67488370-ae42d700-f6aa-11e9-9560-7d848e2e0af2.PNG)

##### Flask로 웹을 구성했기 때문에 Flask를 선택한다.



![pythonanywhereStart3](https://user-images.githubusercontent.com/50854729/67488372-aedb6d80-f6aa-11e9-9dd6-1c0114774f6c.PNG)

##### python 버전을 선택해준다.



![pythonanywhereStart4](https://user-images.githubusercontent.com/50854729/67488373-aedb6d80-f6aa-11e9-9c93-f5e128a03d73.PNG)

##### 웹에서 스크롤을 좀 내리면 화살표로 표시한 버튼이 나온다 클릭해준다.

![pythonanywherefilemanager](https://user-images.githubusercontent.com/50854729/67488364-adaa4080-f6aa-11e9-99b7-277687fa223f.PNG)

flask_app.py를 눌러 자신의 app.py의 코드들을 복사해서 붙여준다.



![pythonanywhereflask_app_py](https://user-images.githubusercontent.com/50854729/67488365-adaa4080-f6aa-11e9-82dc-a2ace22e6850.png)



![newenv](https://user-images.githubusercontent.com/50854729/67549869-2c04f200-f740-11e9-83ac-b6ef90a9b40a.PNG)

##### 화살표로 표시한 입력란에 '.env'를 입력하여 'New file' 버튼을 클릭하여 .env파일을 만들어주고 .env를 클릭하여 자신의 '.env'에 입력된 데이터를 입력해준다.

![pythonanywhere_env](https://user-images.githubusercontent.com/50854729/67488366-adaa4080-f6aa-11e9-9e23-54725d1d6d59.PNG)



##### python anywhere에는 웬만한 라이브러리들을 내장하고 있는데 좀 minor한 python-decouple은 내장하고있지 않아서 설치해주어야 한다.



### 라이브러리 설치


![pythonanywhereconsole](https://user-images.githubusercontent.com/50854729/67488374-af740400-f6aa-11e9-90b8-ca65fb05cb15.PNG)

##### 'Consoles'로 가서 Bash를 클릭해준다.



![pythonanywherepip](https://user-images.githubusercontent.com/50854729/67488379-b00c9a80-f6aa-11e9-9f7b-7b240118f5c1.PNG)

##### python3.74버전이라서 pip3를 사용한다. 

##### pip3 install python-decouple --user를 입력하여 decouple설치해준다.



![reload](https://user-images.githubusercontent.com/50854729/67550328-28259f80-f741-11e9-89d4-5d1b98500211.PNG)

##### 이제 다시 Web으로 가서 초록색 버튼 Reload를 해주면 자신의 컴퓨터에서 flask를 실행하지 않아도 서버를 이용할 수 있다.





## google API(translate)



#### api key 발급

![apikey](https://user-images.githubusercontent.com/50854729/67488978-b6e7dd00-f6ab-11e9-9634-104ebfee9ae3.PNG)





#### api_url 가져오기

![translateAPI](https://user-images.githubusercontent.com/50854729/67488979-b6e7dd00-f6ab-11e9-8df0-d27dc56cb2dd.PNG)

##### 1번주소로 접근하여 2번 api url을 복사한다.



#### api 사용하기(python)

![APIuse](https://user-images.githubusercontent.com/50854729/67488980-b6e7dd00-f6ab-11e9-998e-45bb717e1511.PNG)

##### api_url에 api url을 입력하고 key에 자신의 발급받은 api key를 입력하고 data에 넣은것처럼 q에는 번역하고자 하는 문자열을 source는 해당 문자열의 언어, target에는 번역하고자 하는 언어를 입력하여 requests.port()를 사용할 수 있다.

![translateResult](https://user-images.githubusercontent.com/50854729/67489524-ab48e600-f6ac-11e9-873c-02cde3c3d45d.PNG)

##### result를 출력해보면 'Mother Panda has a baby'가 출력되는걸 확인할 수 있다.