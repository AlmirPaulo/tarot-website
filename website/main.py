from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Page'


#factory
def create_app():
    return app


if __name__=='__main__':
    create_app().run(debug=True)
