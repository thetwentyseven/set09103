from flask import Flask, redirect, url_for, abort
app = Flask(__name__)

@app.route("/")
def root():
 return "The default, 'root' route"

@app.route("/hello/")
def hello():
 return "Hello Napier!!! :D"

# Now I am going to create a 404 error
@app.errorhandler(404)
def page_not_found(error):
  return "Could not find the page you requested.", 404

@app.route("/goodbye/")
def goodbye():
 return "Goodbye cruel world :("


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
