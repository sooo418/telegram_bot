from flask import Flask, render_template, request
from decouple import config
import requests
import random

app = Flask(__name__)

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')

@app.route('/')
def hello_world():
    return 'Hello, World!'

# 텔레그램 서버가 우리 서버에게 HTTP POST 요청을 통해,
# 사용자 메시지 정보를 받아라고 전달해주는 것
# 우리가 status 200을 리턴해줘야 텔레그램 측이 더이상의 전송을 중단한다.
# 200을 안돌려주면 계속~~~ POST 요청을 여러번 보낸다.
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # 1. 메아리(Echo)기능
    # 1.1 request.get_json() 구조 확인하기
    print(request.get_json())
    # 1.2 사용자 아이디, 텍스트 가져오기
    # chat_id = request.get_json().get('message').get('from').get('id')
    text = request.get_json().get('message').get('text')
    print(chat_id, text)
    # 1.3 텔레그램 API에게 요청을 보내서 답변해주기
    api_url = 'https://api.telegram.org'

    # 1. [기본] 로또 기능 (random ... ?)
    # 사용자가 '/로또'라고 말하면 랜덤으로 번호 6개 뽑아서 돌려주기!
    # 나머지 경우엔 전부 메아리 칩시다
    if f'{text}' == '/로또':
        lotto = str(sorted(random.sample(range(1,46),6)))
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={lotto}')
    elif f'{text[0:8]}' == '/vonvon ' and len(text) > 7:
        user_name = text[9:]
        pokemon_list = ['이상해씨', '이상해풀', '이상해꽃', '파이리', '리자드', '리자몽', '꼬부기', '어니부기', '거북왕',
        '캐터피', '단데기', '버터플', '뿔충이', '딱충이'
        ,'독침붕'
        ,'구구'
        ,'피죤'
        ,'피죤투'
        ,'꼬렛'
        ,'레트라'
        ,'깨비참'
        ,'깨비드릴조'
        ,'아보'
        ,'아보크'
        ,'피카츄'
        ,'라이츄'
        ,'모래두지'
        ,'고지'
        ,'니드런♀'
        ,'니드리나'
        ,'니드퀸'
        ,'니드런♂'
        ,'니드리노'
        ,'니드킹'
        ,'삐삐'
        ,'픽시'
        ,'식스테일'
        ,'나인테일'
        ,'푸린'
        ,'푸크린'
        ,'주뱃'
        ,'골뱃'
        ,'뚜벅쵸'
        ,'냄새꼬'
        ,'라플레시'
        ,'파라스'
        ,'파라섹트'
        ,'콘팡'
        ,'도나리'
        ,'디그다'
        ,'닥트리오'
        ,'나옹	'
        ,'페르시온'
        ,'고라파덕'
        ,'골덕'
        ,'망키'
        ,'성원숭'
        ,'가디'
        ,'윈디'
        ,'발챙이'
        ,'슈륙챙이'
        ,'강챙이'
        ,'캐이시'
        ,'윤겔라'
        ,'후딘'
        ,'알통몬'
        ,'근육몬'
        ,'괴력몬'
        ,'모다피'
        ,'우츠동'
        ,'우츠보트'
        ,'왕눈해'
        ,'독파리'
        ,'꼬마돌'
        ,'데구리'
        ,'딱구리'
        ,'포니타'
        ,'날쌩마'
        ,'야돈'
        ,'야도란'
        ,'코일'
        ,'레어코일'
        ,'파오리'
        ,'두두'
        ,'두트리오'
        ,'쥬쥬'
        ,'쥬레곤'
        ,'질퍽이'
        ,'질뻐기'
        ,'셀러'
        ,'파르셀'
        ,'고오스'
        ,'고우스트'
        ,'팬텀'
        ,'롱스톤'
        ,'슬리프'
        ,'슬리퍼'
        ,'크랩'
        ,'킹크랩'
        ,'찌리리공'
        ,'붐볼'
        ,'아라리'
        ,'나시'
        ,'탕구리'
        ,'텅구리'
        ,'시라소몬'
        ,'홍수몬'
        ,'내루미'
        ,'또가스'
        ,'또도가스'
        ,'뿔카노'
        ,'코뿌리'
        ,'럭키'
        ,'덩쿠리'
        ,'캥카'
        ,'쏘드라'
        ,'시드라'
        ,'콘치'
        ,'왕콘치'
        ,'별가사리'
        ,'아쿠스타'
        ,'마임맨'
        ,'스라크'
        ,'루주라'
        ,'에레브'
        ,'마그마'
        ,'쁘사이저'
        ,'켄타로스'
        ,'잉어킹'
        ,'갸라도스'
        ,'라프라스'
        ,'메타몽'
        ,'이브이'
        ,'샤미드'
        ,'쥬피썬더'
        ,'부스터'
        ,'폴리곤'
        ,'암나이트'
        ,'암스타'
        ,'투구'
        ,'투구푸스'
        ,'프테라'
        ,'잠만보'
        ,'프리져'
        ,'썬더'
        ,'파이어'
        ,'미뇽'
        ,'신뇽'
        ,'망나뇽'
        ,'뮤츠'
        ,'뮤']
        # 3. 리스'트에서 랜덤으로 하나씩을 선택한다.
        pokemon = random.choice(pokemon_list)
        if user_name == '최재범':
            pokemon = '잠만보'
        result = f'{user_name}님은 {pokemon}입니다.'    
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={result}')

    else:
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

    # 2. [심화] vonvon 기능
    #    사용자가 '/vonvon 이름'이라고 말하면 신이 나를 만들었을 때 요소 돌려주기!

    return '', 200

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '<h1>메시지 전송 완료!!!!</h1>'

if __name__ == '__main__':
    app.run(debug=True)