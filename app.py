import pickle
import numpy as np
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Load the scaling model and the machine learning model
scaling_model = pickle.load(open('scaling.pkl', 'rb'))
loaded_model = pickle.load(open('logistic_reg_seachCV.pkl', 'rb'))

@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html',)  # Pass 'result=None' initially

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get user inputs from the form
            inputs = {
                'battery_power': int(request.form['battery_power']),
                'blue': 1 if request.form['blue'] == 'yes' else 0,
                'clock_speed': float(request.form['clock_speed']),
                'dual_sim': 1 if request.form['dual_sim'] == 'yes' else 0,
                'fc': int(request.form['fc']),
                'four_g': 1 if request.form['four_g'] == 'yes' else 0,
                'int_memory': int(request.form['int_memory']),
                'm_dep': float(request.form['m_dep']),
                'mobile_wt': int(request.form['mobile_wt']),
                'n_cores': int(request.form['n_cores']),
                'pc': int(request.form['pc']),
                'px_height': int(request.form['px_height']),
                'px_width': int(request.form['px_width']),
                'ram': int(request.form['ram']),
                'sc_h': int(request.form['sc_h']),
                'sc_w': int(request.form['sc_w']),
                'talk_time': int(request.form['talk_time']),
                'three_g': 1 if request.form['three_g'] == 'yes' else 0,
                'touch_screen': 1 if request.form['touch_screen'] == 'yes' else 0,
                'wifi': 1 if request.form['wifi'] == 'yes' else 0
            }
            print(inputs)
            final_data = scaling_model.transform([list(inputs.values())])  # Pass a list of values
            print(final_data)
            # Make predictions using the loaded machine learning model
            predictions = loaded_model.predict(final_data)

            # Return the predicted price range as JSON response
            result = {
                'prediction': predictions[0]
            }

            return jsonify(result)

        except Exception as e:
            return jsonify({'error': str(e)})
        
    
    # Return the predicted price range as JSON response
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
