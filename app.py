from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/qcm')
def qcm():
    return render_template('qcm.html')

@app.route('/resultat', methods=['POST'])
def resultat():
    score = 0
    bor = {
        "q1": "b",
        "q2": "b",
        "q3": "c",
        "q4": "a",
        "q5": "c",
        "q6": "b"
    }

    for key in bor:
        reponse = request.form.get(key)
        if reponse:
            if reponse.strip().lower() == bor[key]:
                score += 1

    return render_template('resultat.html', score=score, total=len(bor))



if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
