from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/resultat', methods=['GET'])
def resultat():
  result = request.args
  n = result['r']
  q = result['g']
  r = result['b']
  p = result['prenom']
  return render_template("resultat.html", r=n, prenom=p, g=q, b=r)


if __name__ == "__main__":
  app.run(host='0.0.0.0', port=81)
