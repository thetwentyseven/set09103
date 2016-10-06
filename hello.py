from flask import Flask
app = Flask(__name__)

@app.route("/hello/<name>")
def hello(name):
 return "Hello %s" % name

# Chapter 4 exercise, using variables


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
