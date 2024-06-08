from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

connect = sqlite3.connect('database.db') 
connect.execute( 
    'CREATE TABLE IF NOT EXISTS PRODUTOS (nome_produto TEXT,\
      valor_produto NUMBER, tipo_despesa TEXT, categoria TEXT, saldo TEXT)')


@app.route('/adicionar_produto', methods=['GET', 'POST']) 
def adicionar_produto(): 
    if request.method == 'POST': 
        nome_produto = request.form['nome_produto'] 
        valor_produto = request.form['valor_produto'] 
        tipo_despesa = request.form['tipo_despesa'] 
        categoria = request.form['categoria'] 
        saldo = request.form['saldo'] 
  
        with sqlite3.connect("database.db") as users: 
            cursor = users.cursor() 
            cursor.execute("INSERT INTO PRODUTOS \
            (nome_produto, valor_produto, tipo_despesa, categoria, saldo) VALUES (?,?,?,?,?)", 
                           (nome_produto, valor_produto, tipo_despesa, categoria, saldo)) 
            users.commit() 
        return redirect(url_for('home'))
    return render_template('adicionar_produto.html')
    

@app.route('/remover_produto', methods=['GET', 'POST'])
def remover_produto():
    if request.method == 'POST':
        nome_produto = request.form['nome_produto']
        with sqlite3.connect("database.db") as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM PRODUTOS WHERE nome_produto = ?", (nome_produto,))
            conn.commit()
        return redirect(url_for('home'))
    connect = sqlite3.connect('database.db') 
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM PRODUTOS') 
  
    data = cursor.fetchall() 
    return render_template('remover_produto.html', data=data)


@app.route("/")
def home():
    connect = sqlite3.connect('database.db') 
    cursor = connect.cursor() 
    cursor.execute('SELECT * FROM PRODUTOS') 
    data = cursor.fetchall()
    return render_template("index.html", data=data)
    
    
if __name__ == "__main__":
    app.run(debug=True)
