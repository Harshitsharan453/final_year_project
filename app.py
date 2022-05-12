import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('C:\\Users\\Harshit\\Desktop\\final_year_project_file\\venv\\model_final.pkl','rb'))

@app.route('/')
def home():
    return render_template('C:\\Users\\Harshit\\Desktop\\final_year_project_file\\web_page.html')

@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()]
    final_features  = [np.array(int_features)]
    prediction = model.predict(final_features)
    
    output = prediction
    return render_template('C:\\Users\\Harshit\\Desktop\\final_year_project_file\\web_page.html',prediction_text = 'File is: {}'.format(output))

if __name__ == "__main__":
    app.run(debug = True)