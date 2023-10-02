
# Employee Attrition Predictor

This is an Employee Attrition Predictor, which predicts the attrition (yes or no) for an employee. The dataset which has been trained for this project was created by the IBM Data Scientists.  

## Tech Stack

**Front End:** HTML, CSS

**Back End:** Flask, Python

**ML Algorithm:** Random Forest Classifier

## Documentation

[Documentation for Random Forest Classifier](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.RandomForestClassifier.html)


## Acknowledgements

 - [Dataset Link](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset)
 - [Colab Notebook](https://colab.research.google.com/drive/1RKgy0O_ktbxEWWM3XkGTmWglk3-ns7xK#scrollTo=9y3_AsjHl8-9)


## Optimizations

To reduce the number of features, the feature selection was carried out to ease the work of the user.


## Run Locally

Clone the project

```bash
  git clone https://github.com/ashutosh1808/employee-attrition-prediction.git
```

Go to the project directory

```bash
  cd employee-attrition-prediction
```

Install dependencies

```bash
    pip install sklearn
```
```bash
    pip install flask
```
```bash
    pip install numpy
```
```bash
    pip install pandas
```

Start the server

```bash
  python app.py
```

