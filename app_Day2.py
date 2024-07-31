### Building Url Dynamically
#### Flask variable Rules And Url Building


from flask import Flask, redirect, url_for


app = Flask(__name__)


@app.route('/')
def welcom():
    return'welcome to'

#### Flask variable Rules And Url Building

@app.route('/success/<int:score>')
def success(score):
    return "the person has paass and the marks is"+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and the marks is"+str(score)

## Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=''
    if marks<50:
        result='fail'
    else:
        result='success'

    return redirect(url_for(result,score=marks))
    # return "the person has failed and the marks is"+str(score)


if __name__=='__main__':
    app.run(debug=True)
