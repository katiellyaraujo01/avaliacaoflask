from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dados em memória
items = []
next_id = 1

@app.route('/')
def index():
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    global next_id
    nome = request.form.get('nome')
    quantidade = request.form.get('quantidade')
    valor = request.form.get('valor')
    items.append({
        'id': next_id,
        'nome': nome,
        'quantidade': int(quantidade),
        'valor': float(valor)
    })
    next_id += 1
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    global items
    if request.method == 'POST':
        nome = request.form.get('nome')
        quantidade = request.form.get('quantidade')
        valor = request.form.get('valor')
        for item in items:
            if item['id'] == id:
                item['nome'] = nome
                item['quantidade'] = int(quantidade)
                item['valor'] = float(valor)
                break
        return redirect(url_for('index'))

    item = next((item for item in items if item['id'] == id), None)
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    global items
    items = [item for item in items if item['id'] != id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
