# Flask Login System

## Sistema de login simples de fácil uso tanto para os devs quanto pros usuários, usando o Flask, Python, e HTML5+CSS3.

## Instalação:

### Pré Requesitos:

## Python 3.9 ou mais recente
## Flask

```bash
pip install Flask
```

## PyMySQL

```bash
pip instal pymysql
```
### OBS: O Werkzeug.security já vem no Flask

## Instruções de uso:

### Passo a passo:

1. Inicialize o app.py
2. Configure a conexão com o seu Banco de Dados
3. Abra o index.html
4. Clique em "Login" ou "Registrar-Se" se não tiver se registrado
5. Continue com o processo

### OBS: Edite o código como quiser, mude os links, os redirects, e personalize o front-end.

### Uso do Python:

Importando o PyMySQL:
```bash
import pymysql as pms
```

Importando o Flask
```bash
from flask import Flask, render_template, request, url_for, redirect
```
Importando o gerador de hash:
```bash
from werkzeug.security import check_password_hash, generate_password_hash
```


Trazendo os objetos HTML para o Python:
```bash
app = Flask(__name__)
```

Definindo a conexão:
```bash
def connection():
    connect = pms.Connection(
        host="localhost",
        user="seu usuário",
        password="sua senha",
        database="seudb",
        charset="utf8mb4",
        cursorclass=pms.cursors.DictCursor,
        port=suaporta
    )

    return connect
```

Trazendo a página Logged:
```bash
@app.route('/logged')
def logged():
    return render_template('logged.html')
```

Importando a rota do register:
```bash
@app.route('/register', methods=['GET', 'POST'])
```

Função do register:
```bash
def register():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')

        if password and email and name:
            p_hash = generate_password_hash(password)

            conn = connection()
            cursor = conn.cursor()

            cursor.execute("INSERT INTO users (username, email, hash) VALUES (%s, %s, %s)", (name, email, p_hash))
            cursor.close()
            conn.commit()

            return redirect(url_for('login'))

    return render_template('register.html')
```

Importando a rota do Login:
```bash
@app.route('/login', methods=['GET', 'POST'])
```

Função de Login:
```bash
def login():
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        conn = connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, hash, username FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and check_password_hash(user['hash'], password):
            return redirect(url_for('logged'))
        else:
            return redirect(url_for('login'))
    
    return render_template('login.html')
```

Deixar o Flask ativo:
```bash
if __name__ == '__main__':
    app.run(debug=True)
```