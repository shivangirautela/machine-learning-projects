from flask import Flask, render_template,request,redirect
from flask.helpers import url_for
import csv
app = Flask(__name__)
print(__name__)

@app.route('/about.html')
def my_home():
    return render_template('about.html')

@app.route('/<string:page_name>')
def html_page(page_name):
     return render_template(page_name)

@app.route('/works.html')
def my_home6():
    return render_template('works.html')

@app.route('/')
def hellohg_world():
    return render_template('index.html')

@app.route('/components.html')
def helljho_w():
    return render_template('components.html')

@app.route('/contact.html')
def hello_world6():
    return render_template('contact.html')

@app.route('/work.html')
def hello_worl():
    return render_template('work.html')

@app.route('/works.html')
def hello_wor():
    return render_template('works.html')

def write_to_file(data):
    with open('database.txt',mode='a')as database: # a for append 
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n {email}, {subject} , {message}') 

def write_to_csv(data):
    with open('database.csv', newline='',mode='a')as database2: # a for append 
        email = data["email"] 
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',',quotechar='"' ,quoting=csv.QUOTE_MINIMAL )
        csv_writer.writerow([email,subject,message]) 

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method =='POST': 
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            print(data)
            return redirect('thankyou.html')
        except:
            return "did not save to the database"
    else:
        return 'something went wrong. try again.'

#---------------------------------------------------------------
""" @app.route('/<username>/<int:post_id>')
def hehgllo_worl(username=None,post_id=None):
      return render_template('index.html',name=username,post_id=post_id)

@app.route('/blog')
def blog1():
    return 'Hello, shivangi rautela this is a blog'

@app.route('/blog/22')
def blog2():
    return 'this is my dog'

@app.route('/abohgut.html')
def abouhvt():
    return render_template('about.html')

@app.route('/favicon/2')
def blog13():
    return 'Hello, shivangi rautela this is a blog'

@app.route('/index.html')
def hellgco_world():
    print(url_for('static', filename='bolt.ico')) # dynamically update websites 
    return render_template('index.html')
 """