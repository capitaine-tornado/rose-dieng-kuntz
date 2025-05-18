from flask import Flask, render_template, request

app = Flask(__name__) #dit que ce sera une appli flask 


@app.route('/')
def index():   #dit quel est la page principale 
    return render_template('index.html')
    
@app.route('/qcm')
def qcm():       #crée le qcm et dit sur quelles pages il sera 
    return render_template('qcm.html')
@app.route('/page2')
def page2():
    return render_template('page2.html')
    
@app.route('/resultat', methods=['POST'])
def resultat():    #définie les résultats du qcm
    score = 0
    bor = {
        "q1": "b",
        "q2": "b",
        "q3": "c",
        "q4": "c",
        "q5": "c",
        "q6": "b"
    }

    for key in bor:  #ajoute 1 au score si le résultat entré par le joueur est le même que celu-ci dessus 
        reponse = request.form.get(key)
        if reponse:
            if reponse.strip().lower() == bor[key]:
                score += 1

    return render_template('resultat.html', score=score, total=len(bor)) #retourne le score sur la page de résultat 



if __name__ == "__main__":    #corrige le bug qui fait le site ne trouve pas le bon port 
  app.run(host='0.0.0.0', port=81)
