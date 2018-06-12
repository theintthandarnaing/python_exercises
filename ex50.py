from flask import Flask
2 app = Flask(__name__)
3
4 @app.route('/')
5 def hello_world():
6 return 'Hello, World!'
7
8 if __name__ == "__main__":
9 app.run()
from flask import Flask
2 from flask import render_template
3
4 app = Flask(__name__)
5
6 @app.route("/")
7 def index():
8 greeting = "Hello World"
9 return render_template("index.html", greeting=greeting)
10
11 if __name__ == "__main__":
12 app.run()
