from sklearn import linear_model
from preprocess import *

def preprocess_train(filename, is_test=False):
    df = get_Merged(filename)
    df = preprocess_type(df)
    df = preprocess_date(df)
    df = preprocess_dept(df)
    if is_test:
        return df
    x,y = send_xy(df)
    return df, x, y


df,x,y = preprocess_train('dataset/trainMerged.csv')

# df.to_csv('dataset/processing_data.csv', index=False)

# reg = linear_model.Ridge (alpha = 1)
reg = linear_model.BayesianRidge()
reg.fit (x, y) 

print(reg.coef_)
print(reg.intercept_)

df_test = preprocess_train('dataset/testMerged.csv',is_test=True)

res = reg.predict(df_test)


send_submission('submit/submit8.csv', res)

# kaggle competitions submit -c walmart-recruiting-store-sales-forecasting -f submit/submit8.csv -m "bayes' model"
