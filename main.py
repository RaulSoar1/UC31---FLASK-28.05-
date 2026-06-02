from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/cadastro", methods=['GET','POST'])
def cadastro():

    mensagem = ""

    if request.method == 'POST':
        nickname = request.form.get('nickname')
        jogo = request.form.get('jogo')
        email = request.form.get('email')

        if not nickname or len(nickname) < 4 or not jogo or not email:
            mensagem = "Preencha todos os campos obrigatórios."
        else:
            mensagem = "Inscrição realizada com sucesso!"

        nome = request.form.get('nome')
        if not nome:
            mensagem = "O campo nome é obrigatório"
        else:
            mensagem = f"cadastro realizado com sucesso!"
    else: 
        mensagem = f"cadastro realizado com sucesso! Bem-vindo, {nome}"
        return render_template('cadastro.html', mensagem=mensagem)
    
    return render_template('cadastro.html', mensagem=mensagem)

if __name__ == '__main__':
    app.run(debug=True)
    
