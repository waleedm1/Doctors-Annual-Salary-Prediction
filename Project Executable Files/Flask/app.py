from flask import *
import pickle
import os
import re
app=Flask(__name__,template_folder='template') 
model = pickle.load(open(r"C:\Users\navyasri\OneDrive\Desktop\soumyasri project\Flask\Doctors Salary Prediction.pkl", 'rb'))
@app.route('/')
@app.route('/home',methods=['GET', 'POST'])
def Home(): 
    return render_template('home.html')

@app.route('/happy', methods=['GET', 'POST']) 

def happy():
   return render_template('prediction.html')

@app.route('/result', methods=['GET', 'POST']) 
def result():
    if request.method == "POST":
       Specialty=request.form['Specialty']
       Feel_Fairly_Compensated=request.form['Feel Fairly Compensated']
       Overall_Career_Satisfaction=request.form['Overall Career Satisfaction']
       Satisfied_Income=request.form['Satisfied Income']
       Would_Choose_Medicine_Again=request.form['Would Choose Medicine Again'] 
       Would_Choose_the_Same_Specialty=request.form['Would Choose the Same Specialty']
       Survey_Respondents_by_Specialty=request.form['Survey Respondents by Specialty']
       pred = [[float(Specialty), 
         float (Feel_Fairly_Compensated),
           float (Overall_Career_Satisfaction), 
           float (Satisfied_Income),
             float(Would_Choose_Medicine_Again),
               float (Would_Choose_the_Same_Specialty), 
               float (Survey_Respondents_by_Specialty)]]
    print (pred)
    output = model.predict(pred)
    print(output)
    return render_template('result.html', predict= output)
if __name__ == '__main__':
 app.run(debug=True)
