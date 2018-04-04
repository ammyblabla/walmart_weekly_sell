import pandas as pd
from preprocess import get_trainMerged, preprocess_type, send_xy

d = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd']),
    'three' : pd.Series(['A', 'B', 'A', 'B'], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)