from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
@app.route('/calculate', methods=['POST'])
def calculate():
    expression = request.form['expression']
    if not expression:
        return render_template('index.html', result=None, expression="")
    
    try:
        result = eval(expression)  # Avalia a expressão matemática enviada
        return render_template('index.html', result=result, expression=expression)
    except:
        return render_template('index.html', result="Erro", expression=expression)
    
if __name__ == '__main__':
    app.run(debug=True)
