from flask import Flask, render_template, url_for

app = Flask(__name__)

#Start
@app.route('/')
def first():
    return render_template('index.html')

#Tier 1
#At clock
@app.route('/clock')
def clock():
    return render_template('clock.html')

#Tier 2
#Outside CCA room
@app.route('/mcroom') 
def mentoringclub():
    return render_template('room.html')

#Snack corner
@app.route('/snack')
def snack():
    return render_template('snack.html')

#Tier 3
#Pillar
@app.route('/pillar') 
def pillar():
    return render_template('pillar.html')

#Pillar with bins
@app.route('/pillarbins')
def pillarbins():
    return render_template('pillarbins.html')

#Lift
@app.route('/lift') 
def lift():
    return render_template('lift.html')

#Event venue
@app.route('/event')
def event():
    return render_template('event.html')

#Tier 4
#Displayed on computer while I sleep
@app.route('/comp') 
def comp():
    return render_template('comp.html')

#Displayed near vending machine
@app.route('/vend')
def vend():
    return render_template('vend.html')

#Final Main - Placed at xxx
@app.route('/random') 
def location():
    return render_template('random.html')

#####################################################
#Wrong place
#Stairs
@app.route('/stairs')
def stairs():
    return render_template('stairs.html')

#####################################################
#Decoy Sites
@app.route('/d3c0y')
def decoy1():
    return render_template('decoys/decoy1.html')

@app.route('/dec0y')
def decoy2():
    return "Decoy"

#####################################################
if __name__ == '__main__':
  app.run(debug=True)