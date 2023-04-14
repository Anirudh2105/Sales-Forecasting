from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from prophet import Prophet
from prophet.plot import plot_plotly, plot_components_plotly
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os
from flask import Flask, send_from_directory
import datetime
from sklearn.metrics import mean_squared_error, mean_absolute_percentage_error

app = Flask(__name__, static_folder='webapp/src')
CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']

    if not file or (file.content_type != 'text/csv' and file.content_type != 'application/vnd.ms-excel' and file.content_type != 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'):
        return jsonify({'message': 'Invalid file type.'}), 400

    # Data Upload and pre processing
    df = pd.read_csv(file)
    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    df.head()
    df.columns = ["ds", "y"]

    # Change the date to datetime object
    df["ds"] = pd.to_datetime(df["ds"])
    # df["ds"] = pd.to_datetime(df["ds"], format="%d/%m/%Y")

    #Getting the Numerix and Periodicity

    Numerix = int(request.form.get('selectedNumerix'))
    periodicity = request.form.get('selectedPeriodicity')

    if periodicity == "Daily":
        periodicity = "D"
    
    elif periodicity == "Weekly":
        periodicity = "W"

    elif periodicity == "Monthly":
        periodicity = "MS"
    
    elif periodicity == "Yearly":
        periodicity = "A"

    #Plotting the input data
    df.plot(x="ds", y="y", figsize=(10, 6))
    length = len(df)
    train_size = round((80 / 100) * length)
    train = df[: train_size]
    train.tail()

    #Prediction of the data
    
    m = Prophet()
    m.fit(df)
    future = m.make_future_dataframe(periods=Numerix, freq=periodicity)
    forecast = m.predict(future)
    thecsv = pd.DataFrame({'Date': forecast['ds'], 'Sales': forecast['yhat']})
    thecsv.to_csv('Final_total_output.csv', index=False)


    # For plotting the old and forcasted data

    fpp = forecast.tail(Numerix) 

    thecsv = pd.DataFrame({'Date': forecast['ds'], 'Sales': forecast['yhat']})

    for_pred =  pd.DataFrame(forecast.head( len(forecast) - Numerix))
    for_pred1 = pd.DataFrame({'ds': for_pred['ds'], 'yhat': for_pred['yhat']})

    for_preds =  pd.DataFrame({'ds': for_pred1['ds'], 'yhat': for_pred1['yhat']})
    ecp = pd.DataFrame({'ds': for_preds['ds'], 'yhat': for_preds['yhat']})
    ecp1 = pd.DataFrame({'ds': fpp['ds'], 'yhat': fpp['yhat']})
    plt.plot(ecp['ds'], ecp['yhat'], label='Actual')
    plt.plot(ecp1['ds'], ecp1['yhat'], label='Predicted')
    plt.legend()
    plt.xlabel("DATE")
    plt.ylabel("SALES")
    plt.savefig(os.path.join(app.static_folder, 'assets', 'pastforecast.png'),dpi=300, bbox_inches = 'tight') 
    plt.show() 
    plt.close()
    
    
    fcp = pd.DataFrame({'ds': fpp['ds'], 'y': fpp['yhat']})
    fcp = fcp.set_index("ds")
    print(fcp)

    table_pred = pd.DataFrame({'Date': fpp['ds'], 'Sales': fpp['yhat']})
    table_pred = table_pred.set_index("Date")
    table_pred.to_csv(os.path.join(app.static_folder, 'assets', 'Predicted_result.csv'))
    
    fcp.plot(figsize=(10, 6))
    plt.title("The Predicted data based on the given dataset")
    plt.grid()
    plt.xlabel('DATE')
    plt.ylabel('SALES')
    plt.grid()
    plt.savefig(os.path.join(app.static_folder, 'assets', 'prediction.png'), dpi=300, bbox_inches='tight') 
    plt.show()
    plt.close()    



    fig = plot_plotly(m, forecast)

    fig.write_html("static/assets/forecast.html")

    # Finding out the trend

    fig2 = m.plot_components(forecast)

    fig2.savefig(os.path.join(app.static_folder, 'assets', 'Trends.png'))

    # """EVALUATING THE MODEL


    # Calculate RMSE and MAPE
    actual = df['y'].tail(Numerix)
    predicted = fpp['yhat']
    rmse = mean_squared_error(actual, predicted, squared=False)
    mape = mean_absolute_percentage_error(actual, predicted)

    # Print RMSE and MAPE
    print("RMSE:", rmse)
    print("MAPE:", mape)



    return jsonify({'message': 'File uploaded successfully.'}), 200


if __name__ == '__main__':
    app.run(debug=True)