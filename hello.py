from flask import Flask, request
app = Flask(__name__)

# Chapter 4.1.4, url and parameters
@app.route("/hello/")
def hello():
  name = request.args.get('name','')
  if name == '':
    return "No parameters supplied"
  else:
    return "Hello %s" % name

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
