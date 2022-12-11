## 아래 주석 처리한 공간에서 본인이 필요한 기능의 코드를 작성해주시면 됩니다.
## HTML 파일은 작업 중간중간 아무 때나 커밋하셔도 상관 없습니다.
## Python 파일은 추후 정해진 시간에 각각 순차적으로 업로드할 예정입니다.


# Packages
## 이 곳에서'만' 패키지를 받아옵니다.
from flask import Flask, render_template, jsonify, request, session, redirect, url_for

app = Flask(__name__)

from pymongo import MongoClient
import certifi
import jwt
import datetime
import hashlib
ca = certifi.where()
client = MongoClient("mongodb+srv://sparta:test@cluster0.xskerwx.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.dbdraft99
SECRET_KEY = 'SPARTA'



# main (상휘)

# join (상휘)

# login (상휘)

# review (정기)
@app.route('/')
def home():
    return render_template('review.html')


@app.route("/library/write", methods=["POST"])
def posting():
    url_receive = request.form['url_give']
    reviewcomment_receive = request.form['reviewcomment_give']

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url_receive, headers=headers)

    soup = BeautifulSoup(data.text, 'html.parser')

    title = soup.select_one('meta[property="og:title"]')['content']
    image = soup.select_one('meta[property="og:image"]')['content']
    desc = soup.select_one('meta[property="og:description"]')['content']

    doc ={
        'title':title,
        'image':image,
        'desc':desc,
        'reviewcomment':reviewcomment_receive
    }
    db.reviews.insert_one(doc)

    return jsonify({'msg':'저장 완료!'})
# commentList (지영)

# myPage (경은)
