from flask import Flask, render_template  
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, migrate

app = Flask(__name__)

# adicionando configuração para usar uma database sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

# criando uma instância sqlalchemy
db = SQLAlchemy(app)

# configurações para migrations
migrate = Migrate(app, db)

# Models
class Aplicativo(db.Model):
    valor_produto = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(50), unique=False, nullable=False)
    tipo_despesa = db.Column(db.String(30), unique=False, nullable=False)
    categoria = db.Column(db.String(30), unique=False, nullable=False)
    saldo = db.Column(db.String(3), unique=False, nullable=False)

    def __repr__(self):
        return f"Valor : {self.valor_produto}, Saldo: {self.saldo}"

@app.route("/")
def home():
    return render_template("index.html")
    
    
if __name__ == "__main__":
    app.run(debug=True)
