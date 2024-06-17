from flask import Flask, render_template, request, url_for
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.exception import CustomException
import sys

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/predictdata', methods=['GET', 'POST'])
def predictdata():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        try:
            data = CustomData(
                Number_of_Customers=request.form.get('Number_of_Customers'),
                Menu_Price=request.form.get('Menu_Price'),
                Marketing_Spend=request.form.get('Marketing_Spend'),
                Cuisine_Type=request.form.get('Cuisine_Type'),
                Average_Customer_Spending=request.form.get('Average_Customer_Spending'),
                Promotions=request.form.get('Promotions'),
                Reviews=request.form.get('Reviews')
            )

            pred_df = data.get_data_as_dataframe()
            print(pred_df)
            print('Before Prediction')
            predict_pipeline = PredictPipeline()
            print('Mid Prediction')
            results = predict_pipeline.predict(pred_df)
            print("after Prediction")

            return render_template('home.html', results=results[0], request=request)

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    app.run(host="0.0.0.0")