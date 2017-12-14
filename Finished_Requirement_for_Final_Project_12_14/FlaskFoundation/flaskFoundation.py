# Flask fundamental usage - quick review tutorial

# import other flask installed libraries for differnt usage
from flask import Flask
from flask import Flask, redirect, render_template, request, session, abort, url_for

import random

app = Flask(__name__)


# # The way to contain and use static files like .js, .css in flask (its incorporated and written in the template 'index.html')
# @app.route("/") # means the home root(index page) of the url, adding in URL roots
# def index():
# 	return render_template("index.html")

###### Clear Simple Example of getting in user inputs and rendering them to the templates, while switching corresponding templates and url
# Important info also embedded in the front end html
@app.route('/')
def student():
   return render_template('student.html') # this template has the actions of directing urls in the <form action="url_to_direct">

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      return render_template("result.html",result = result)
######

@app.route("/hello") # different web router routes
def hello():
	return "Hello Flask!"

@app.route("/members")
def members():
	return "Members"

@app.route("/members/<string:name>/") ## the dynamic changes of url route
def getMember(name): # takes the inputs from the url and pass it in the python script to process and render later on
	return render_template(
		"test.html", name=name)  # the render method that renders the "test.html" file within the /"templates"/ directory with the input name var from the url

# @app.route('/hello/<name>')
# def hello_name(name):
#    return 'Hello %s!' % name


# Examples of Dynamic URL building with url_for()
@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest

@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin')) # that is the "function name" in quotes, the later is the variables to be passed into the function parameter as argument
   else:
      return redirect(url_for('hello_guest',guest = name))

# aligned with the lgoin.html in templates
# This part uses the POST, GET HTTP methods to send data to and from the server from the frontend
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route("/tologin", methods=['POST','GET'])
def toLogin():
	return render_template("login.html")


@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm'] #the 'name = "nm"' on the login.html, takes in the input from user and save it as the variable nm on the <form>
      return redirect(url_for('success',name = user)) # redirect this to the above url function
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))

# renders template by passing values in the variable to the front-end variable name 'name'
# @app.route('/hello/<user>')
# def hello_name(user):
#    return render_template('hello.html', name = user) # the front-end variable name in {{name}}

# Jinja2 template engine delimiters for HTML
# {% ... %} for Statements
# {{ ... }} for Expressions to print to the template output
# {# ... #} for Comments not included in the template output
# # ... ## for Line Statements

# Eaxmples ---- with its corresponding templates: see the templates name in the render_template() function to have a better understanding
# using for loops and dictionary info render in the template frontend example
# @app.route('/result')
# def result():
#    dict = {'phy':50,'che':60,'maths':70}
#    return render_template('result.html', result = dict)

# If statements in the front-end
@app.route('/hello/<int:score>')
def hello_name(score):
   return render_template('hello.html', marks = score)


# Important attributes of request object are listed below −

# Form − It is a dictionary object containing key and value pairs of form parameters and their values.

# args − parsed contents of query string which is part of URL after question mark (?).

# Cookies − dictionary object holding Cookie names and values.

# files − data pertaining to uploaded file.

# method − current request method.



@app.route("/AnotherRender")
def AnotherRender():
	#    return name
    quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
               "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
               "'To understand recursion you must first understand recursion..' -- Unknown",
               "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
               "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
               "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"  ]
    randomNumber = random.randint(0,len(quotes)-1) 
    quote = quotes[randomNumber] 
	# The render_template method that renders HTML template in the "templates" folder (in the same folder) according to the function to the frontend 
    return render_template(
        'test.html',**locals()) # the **locals() means to pass mutiple variables to the function, so the author says in an over simplified explanation

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True) # run the server of the webapp, self define ip and port to run, port=????


