from flask import Flask
from urllib import request
from bs4 import BeautifulSoup

# 웹 서버를 생성합니다.
app = Flask(__name__)
@app.route("/")

def hello():
    # urlopen() 함수로 기상청의 전국 날씨를 읽음.
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    # beautifulSoup 사용 웹 페이지 분석
    soup = BeautifulSoup(target, "html.parser")

    # location 태그 읽기
    # location 태그 내부의 정보를 가져 옴
    output = ""
    for location in soup.select("location"):
        # 내부의 city, wf, tmn, tmx 태그를 찾아 출력
        output += "<h3>{}</h3>".format(location.select_one("city").string) # location 내부의 도시, 날씨, 최저기온, 최고기온
        output += "날씨: {}</br>".format(location.select_one("wf").string)
        output += "최저/최고 기온: {}/{}".format(location.select_one("tmn").string, location.select_one("tmx").string)
        output += "<hr/>"

    return output

# set FLASK_ENV=development
# set FLASK_APP=7_2_ex (파일 이름. "7_2_ex" 이런 식으로 문자열 형태로 들어가게 되면 에러)
# flask run