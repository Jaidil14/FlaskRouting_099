from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def home() :
    return render_template('index.html')

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    