from flask import Flask
from support import views

app = Flask(__name__)

# route 방식
# @app.route("/")
# def index():
#     return "첫 번째 Flask 페이지"


# @app.route("/page1")
# def page1():
#     return "page 1"


# @app.route("/page2")
# def page2():
#     return "page 2"

app.add_url_rule('/', 'index', views.index) # / 주소는 index이름이고 views.index로 연결

if __name__ == "__main__":
    app.run()