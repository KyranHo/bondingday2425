from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def first():
    return render_template('index.html')

@app.route('/room')
def mentoringclub():
    return render_template('room.html')

@app.route('/lift')
def lift():
    return render_template('lift.html')


#####################################################

@app.route('/d3c0y')
def decoy1():
    return render_template('decoy1.html')

#####################################################
if __name__ == '__main__':
  app.run(debug=True)
