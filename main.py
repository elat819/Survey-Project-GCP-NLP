from flask import Flask,redirect,render_template,request,url_for
 
app = Flask(__name__)

@app.route('/')
def my_form():
    return redirect(url_for('form'))

@app.route('/form')
def form():
    return render_template('form.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html',form_data = form_data)
 
app.run(host='127.0.0.1', port=8080, debug=True)
