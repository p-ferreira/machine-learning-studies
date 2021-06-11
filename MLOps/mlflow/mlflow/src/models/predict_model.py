import pandas as pd
import mlflow
logged_model = 'file:///C:/Users/PedroFerreira/PycharmProjects/data-science-studies/Machine%20Learning/MLOps/mlflow/mlflow/src/models/mlruns/1/16a52afc54c041b1be6dec7d0f1a375d/artifacts/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.

data = pd.read_csv('../../data/processed/data_X.csv')

predicted = loaded_model.predict(data)

data['predicted'] = predicted

data.to_csv('../../prices.csv')
