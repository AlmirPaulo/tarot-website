from flask import Flask, render_template, jsonify, request, flash, redirect
from flask_mail import Mail, Message
from data import *
import random, config, requests, os,logging


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s:%(module)s:%(levelname)s:%(message)s')

app = Flask(__name__)
mail = Mail()

@app.route("/")
def home():
    return render_template("index.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404


@app.route("/cards")
def cards():
    return render_template("cards.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/yourcard")
def your_card():
    pick = random.randint(0, 21)
    pic = f"imgs/cards/rws/{str(pick)}.jpg"
    res = requests.get("http://localhost:5000/api")
    data = res.json()

    return render_template("card.html", pick=pick, pic=pic, data=data)


@app.route("/docs")
def api_docs():
    return render_template("docs.html")


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
        JUDGMENT,
        WORLD,
    ]
    return jsonify(json)

@app.route('/email', methods=['POST'])
def email():
    if request.method == 'POST' and request.headers['Referer'] == 'http://localhost:5000/about': #prod: config.HOMEPAGE

        #Getting data
        email = request.form.get('email')
        subject = request.form.get('subject')
        text = request.form.get('text')
        if len(email) > 255 or len(subject) > 255 or len(text) > 1000:
            flash('This message is too long!')

        #Sending email
        msg = Message(f'{subject} - {email}')
        msg.body = text
        msg.recipients = [config.MAIL_DEFAULT_SENDER]
        mail.send(msg)
        
        logging.info('email sent')

        flash('Email sent')
        return redirect('/about')
    # prod: return redirect(config.HOMEPAGE)

    else:
        logging.warning(request.headers['Referer'])
        return "I'm sorry I can't help you."

# factory
def create_app():
    #Change it in prod
    app.config['SECRET_KEY'] = os.urandom(32)
    app.config['MAIL_SERVER'] = config.MAIL_SERVER
    app.config['MAIL_PORT'] = config.MAIL_PORT
    app.config['MAIL_USE_TLS'] = config.MAIL_USE_TLS
    app.config['MAIL_USE_SSL'] = config.MAIL_USE_SSL
    app.config['MAIL_USERNAME'] = config.MAIL_USERNAME
    app.config['MAIL_PASSWORD'] = config.MAIL_PASSWORD
    app.config['MAIL_DEFAULT_SENDER'] = config.MAIL_DEFAULT_SENDER
    app.config['MAIL_MAX_EMAILS'] = config.MAIL_MAX_EMAILS
    app.config['MAIL_ASCII_ATTACHMENTS'] = config.MAIL_ASCII_ATTACHMENTS

    mail.init_app(app)
    return app


if __name__ == "__main__":
    create_app().run(debug=True)
