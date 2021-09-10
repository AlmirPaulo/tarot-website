from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


#factory
def create_app():
    return app


if __name__=='__main__':
    create_app().run(debug=True)
