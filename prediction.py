import pandas as pd
data= pd.read_csv("train.csv")
test= pd.read_csv("train.csv")

def clean(data):
    data=data.drop(["Name", "Ticket", "Cabin", "PassengerId"], axis=1)

    cols= ["SibSp", "Parch", "Fare", "Age"]
    for col in cols:
        data[col].fillna(data[col].median(), inplace=True)

    data.Embarked.fillna("U", inplace= True)
    return data

data= clean(data)
test= clean(test)
# with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
#     print(data)

