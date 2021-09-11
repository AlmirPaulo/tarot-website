from flask import Flask, render_template, jsonify, request, redirect, url_for
from data import *
import random, requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

@app.route("/cards")
def cards():
    return render_template("cards.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/yourcard")
def your_card():
    pick = random.randint(0, 21)
    pic = f"imgs/cards/rws/{str(pick)}.jpg"
    res = requests.get("http://localhost:5000/api")
    data = res.json()

    return render_template("card.html", pick=pick, pic=pic, data=data)

@app.route('/docs')
def api_docs():
    return render_template('docs.html')

@app.route("/api")
def get_data():
    json = [
        FOOL,
        MAGICIAN,
        HIGH_PRIESTESS,
        EMPRESS,
        EMPEROR,
        HIEROPHANT,
        LOVERS,
        CHARIOT,
        STRENGTH,
        HERMIT,
        WHEEL,
        JUSTICE,
        HANGED_MAN,
        DEATH,
        TEMPERANCE,
        DEVIL,
        TOWER,
        STAR,
        MOON,
        SUN,
        JUDGEMENT,
        WORLD,
    ]
    return jsonify(json)


# factory
def create_app():
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
