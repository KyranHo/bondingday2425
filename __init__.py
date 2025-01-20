from flask import Flask, render_template, url_for

app = Flask(__name__)

#Start
@app.route('/')
def first():
    return render_template('index.html')

#At clock
@app.route('/Clock')
def clock():
    return render_template('clock.html')


@app.route('/lift') 
def lift():
    return render_template('lift.html')


@app.route('/room') 
def mentoringclub():
    return render_template('room.html')


@app.route('/comp') 
def comp():
    return render_template('comp.html')


@app.route('/pillar') 
def pillar():
    return render_template('pillar.html')

#Final Main - Placed at xxx
@app.route('/random') 
def location():
    return 'lol'

#####################################################
#Decoy Sites
@app.route('/d3c0y') #Placed at corner of E.318
def decoy1():
    return render_template('decoy1.html')

@app.route('/dec0y') #Placed at
def decoy2():
    return "Decoy"

#####################################################
if __name__ == '__main__':
  app.run(debug=True)
