from sklearn import linear_model
from preprocess import *

df,x,y = preprocess_train('dataset/trainMerged.csv')

# df.to_csv('dataset/processing_data.csv', index=False)

reg = linear_model.Ridge (alpha = .5)
reg.fit (x, y) 


print(reg.coef_)
print(reg.intercept_)

df_test = preprocess_test('dataset/testMerged.csv')

res = reg.predict(df_test)

send_submission('dataset/submit1.csv')
