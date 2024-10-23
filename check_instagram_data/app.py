from flask import Flask, render_template, request, redirect, url_for, flash
from programs.get_followers import get_followers_list
import instaloader

L = instaloader.Instaloader()
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success')
def loginSuccess():
    username = request.args.get('username')
    password = request.args.get('password')
    return render_template('login-successful.html',username=username, password=password)

# Gestisce l'invio del form
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Ottieni i dati del form dal request object
        username = request.form['username']
        password = request.form['password']
        
        try:
            # Effettua il login con Instaloader
            L.login(username, password)
            flash("Login avvenuto con successo", "success")
            return redirect(url_for('loginSuccess', username=username, password=password))
        except instaloader.exceptions.BadCredentialsException:
            flash("Incorrect username or password. Please try again.", "error")
            return redirect(url_for('home'))  # Torna alla homepage con errore
        except Exception as e:
            flash(f"An error occurred: {str(e)}", "error")
            return redirect(url_for('home'))
        
@app.route('/operations')
def operations():
    return render_template('operations.html')

@app.route('/get_followers', methods=['POST'])
def get_followers():
    return get_followers_list()

if __name__ == '__main__':
    app.run(debug=True)
