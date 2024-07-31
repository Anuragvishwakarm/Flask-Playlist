from flask import Flask

### WSGI Application

app=Flask(__name__)

@app.route('/')
def welcom():
    return'Welcom to my flask project2'

@app.route('/member')
def member():
    return'Welcom to my member project2'

if __name__=='__main__':
    app.run(debug=True)