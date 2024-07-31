from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcom():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = "pass" if score >= 50 else "fail"
    return render_template('result.html', result=res, score=score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed and the marks are " + str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result = 'fail' if marks < 50 else 'success'
    return redirect(url_for(result, score=marks))

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        science = float(request.form.get('science', 0))
        math = float(request.form.get('math', 0))
        c = float(request.form.get('c', 0))
        DataScienc = float(request.form.get('DataScienc', 0))

        total_score = (science + math + DataScienc + c) / 4

        res = 'success' if total_score >= 50 else 'fail'
        return redirect(url_for(res, score=total_score))
if __name__ == '__main__': 
    app.run(debug=True) 
