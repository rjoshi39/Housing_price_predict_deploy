from flask import *
import pickle
import numpy as np



app = Flask(__name__, static_url_path='/static')
model = pickle.load(open('Housing_price_predict_model.pkl', 'rb'))
@app.route('/')
def Home():
    return render_template('House_price.html')
	


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('House_price.html', results='Price of house should be $ {}'.format(output))
	
	

if __name__ == "__main__":
    app.run(debug=True)
	
	