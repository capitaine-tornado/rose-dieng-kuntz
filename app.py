from flask import Flask, render_template, request

app = Flask(__name__)

# Page du formulaire
@app.route('/')
def index():
    return render_template('index.html')

# Page de résultat
@app.route('/resultat', methods=['POST'])
def resultat():
    score = 0
    bonnes_reponses = {
        "q1": "b",
        "q2": "b",
        "q3": "c",
        "q4": "web sémantique",
        "q5": "c",
        "q6": "b"
    }

    for key in bonnes_reponses:
        reponse = request.form.get(key)
        if reponse:
            if reponse.strip().lower() == bonnes_reponses[key]:
                score += 1

    return render_template('resultat.html', score=score, total=len(bonnes_reponses))
