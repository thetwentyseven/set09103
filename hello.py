from flask import Flask
app = Flask(__name__)

# Chapter 4.1.3, using other variable types (int, and floats)
@app.route("/add/<int:first>/<int:second>")
def add(first, second):
 return str(first+second)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
