from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def first():
    return render_template('index.html')

@app.route('/room')
def mentoringclub():
    return render_template('room.html')

if __name__ == '__main__':
  app.run()
