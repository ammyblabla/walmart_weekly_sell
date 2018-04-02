# train!
from sklearn import linear_model

from preprocess import get_trainMerged, preprocess_type, send_xy

df = get_trainMerged()
df = preprocess_type(df)

reg = linear_model.Ridge (alpha = .5)
x,y = send_xy(df)
reg.fit (x, y) 
# Ridge(alpha=0.5, copy_X=True, fit_intercept=True, max_iter=None,
#       normalize=False, random_state=None, solver='auto', tol=0.001)
print(reg.coef_)
# array([ 0.34545455,  0.34545455])
print(reg.intercept_)
# 0.13636...