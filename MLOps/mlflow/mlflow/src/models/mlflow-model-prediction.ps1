mlflow models predict `
    -m 'runs:/16a52afc54c041b1be6dec7d0f1a375d/model' `
    -i '../../data/processed/data_X.csv' `
    -t 'csv' `
    -o '../../prices2.csv' `
    --no-conda