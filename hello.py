from flask import Flask, render_template
app = Flask(__name__)

# Chapter 5.0.3, using particular templates for particular moments
@app.route('/users/')
def users():
  names = ['Simon', 'Thomas', 'Lee', 'Jamie', 'Sylvester']
  return render_template('loops.html', name=names)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
