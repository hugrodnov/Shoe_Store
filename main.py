from flask import Flask, render_template, redirect, url_for, flash, abort
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventario.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# configure table
class Gorras(db.Model):
    __tablename__ = "gorras"
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    img_url_1 = db.Column(db.String(500), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Ropas(db.Model):
    __tablename__ = "ropas"
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    img_url_1 = db.Column(db.String(500), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Chanclas(db.Model):
    __tablename__ = "chanclas"
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    img_url_1 = db.Column(db.String(500), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


class Tennis(db.Model):
    __tablename__ = "tennis"
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    img_url_1 = db.Column(db.String(500), nullable=False)
    img_url_2 = db.Column(db.String(500), nullable=False)
    size = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)


# db.create_all()


@app.route('/')
def main():
    flip_flops = Chanclas.query.all()
    hats = Gorras.query.all()
    tennis = Tennis.query.all()

    return render_template("index.html", all_flip_flops=flip_flops, all_hats=hats, all_tenis=tennis)


@app.route('/ropas')
def all_ropas():
    ropas = Ropas.query.all()
    return render_template("all_ropas.html", all_ropas=ropas)


@app.route('/chanclas')
def all_chanclas():
    chanclas = Chanclas.query.all()
    return render_template("all_chanclas.html", all_chanclas=chanclas)


@app.route('/gorras')
def all_hats():
    hats = Gorras.query.all()
    return render_template("all_hats.html", all_hats=hats)


@app.route("/tenis")
def all_tennis():
    tennis = Tennis.query.all()
    return render_template("all_tennis.html", todos_los_tennis=tennis)


@app.route('/tenis_show/<int:tenis_id>', methods=["GET", "POST"])
def show_tenis(tenis_id):
    requested_tenis = Tennis.query.get(tenis_id)
    return render_template("single-tenis.html", tennis=requested_tenis)


@app.route('/chanclas_show/<int:chanclas_id>', methods=["GET", "POST"])
def show_chanclas(chanclas_id):
    requested_chanclas = Chanclas.query.get(chanclas_id)
    return render_template("single-chanclas.html", chanclas=requested_chanclas)


@app.route('/gorras_show/<int:gorras_id>', methods=["GET", "POST"])
def show_gorras(gorras_id):
    requested_gorras = Gorras.query.get(gorras_id)
    return render_template("single-gorras.html", gorras=requested_gorras)


@app.route('/ropas_show/<int:ropas_id>', methods=["GET", "POST"])
def show_ropas(ropas_id):
    requested_ropas = Ropas.query.get(ropas_id)
    return render_template("single-ropas.html", ropas=requested_ropas)

if __name__ == "__main__":
    app.run(debug=True)
