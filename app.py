from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_ici'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/realisations')
def realisations():
    return render_template('realisations.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/a-propos')
def a_propos():
    return render_template('a_propos.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        nom = request.form.get('nom')
        email = request.form.get('email')
        message = request.form.get('message')
        
        flash(f"Merci {nom}, votre demande de devis a bien été envoyée. Nous vous recontacterons rapidement !", "success")
        return redirect(url_for('contact'))
        
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)