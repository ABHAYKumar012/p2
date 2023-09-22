import time
import cv2 
from flask import Flask, render_template, Response, flash, request,url_for,redirect

import mediapipe as mp
import numpy as np
from forms import UserInfoForm
import algo

 
from project import exerciseAI, yogaAI  

#-----------------Routing----------------------------------

app = Flask(__name__) 
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '945a61eeffcee883e3b261a47b31ae47'


@app.route('/')   
def index():
    return render_template('index.html') 

@app.route('/exercise/biceps-curl')  
def exerciseBicepsCurl():      
    return render_template('exerciseBicepsCurl.html')    

@app.route('/exercise/push-ups') 
def exercisePushUps():       
    return render_template('exercisePushUps.html')       

@app.route('/exercise/triceps')  
def exerciseTriceps():        
    return render_template('exerciseTriceps.html')    

@app.route('/exercise/squats')  
def exerciseSquats():       
    return render_template('exerciseSquats.html')   

@app.route('/yoga/t-pose')
def yogaT():
    return render_template('yogaT.html') 

@app.route('/yoga/tree-pose')    
def yogaTree():          
    return render_template('yogaTree.html')  

@app.route('/yoga/warrior-pose')      
def yogaWarrior():          
    return render_template('yogaWarrior.html')  

@app.route('/about')  
def about(): 
    return render_template('about.html')  
@app.route('/bmi')
def bmi():
    return render_template('bmi.html')
@app.route('/home',methods=['GET','POST'])
def home():
	form=UserInfoForm()
	if form.validate_on_submit():
		if request.method=='POST':
			name=request.form['name']
			weight=float(request.form['weight'])
			height=float(request.form['height'])
			age=int(request.form['age'])
			gender=request.form['gender']
			phys_act=request.form['physical_activity']

			tdee=algo.calc_tdee(name,weight,height,age,gender,phys_act)
			return redirect(url_for('result',tdee=tdee))

	return render_template('home.html',title="Diet App",form=form)

@app.route('/result',methods=['GET','POST'])
def result():
	tdee=request.args.get('tdee')
	if tdee is None:
		return render_template('error.html',title="Error Page")
	
	tdee=float(tdee)
	breakfast= algo.bfcalc(tdee)
	snack1=algo.s1calc(tdee)
	lunch=algo.lcalc(tdee)
	snack2=algo.s2calc(tdee)
	dinner=algo.dcalc(tdee)
	snack3=algo.s3calc(tdee)
	return render_template('result.html',title="Result",breakfast=breakfast,snack1=snack1,lunch=lunch,snack2=snack2,dinner=dinner,snack3=snack3)

#-----------------Video-Feeds--------------------------------- 
  
@app.route('/bicepCurl_feed')  
def bicepCurl_feed(): 
    return Response(exerciseAI.bicepCurl.gen(), mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/pushUps_feed')  
def pushUps_feed(): 
    return Response(exerciseAI.pushUps.gen(), mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/triceps_feed')        
def triceps_feed(): 
    return Response(exerciseAI.triceps.gen(), mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/squats_feed')    
def squats_feed(): 
    return Response(exerciseAI.squats.gen(), mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/tPose_feed') 
def tPose_feed(): 
    return Response(yogaAI.tPose.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')  

@app.route('/treePose_feed')  
def treePose_feed():  
    return Response(yogaAI.treePose.gen() ,mimetype='multipart/x-mixed-replace; boundary=frame')         
 
@app.route('/warriorPose_feed')                  
def warriorPose_feed():    
    return Response(yogaAI.warriorPose.gen() ,mimetype='multipart/x-mixed-replace; boundary=frame')         
 
#--------------------------------------------------------------
if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')   