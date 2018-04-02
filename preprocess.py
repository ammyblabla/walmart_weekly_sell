import pandas as pd
# read data
def get_trainMerged():
    df = pd.read_csv('dataset/trainMerged.csv')
    df = df.drop(columns=['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5','CPI','Unemployment'])
    return  df
# print(df)

# preprocess
def preprocess_type(df):
    for row in df:
        if df.Type == 'A':
            row['typeA'] = 1
            row['typeB'] = 0
        elif df.Type == 'B':
            row['typeA'] = 0
            row['typeB'] = 1
    df.drop(columns=['Type'])
    return df

def send_xy(df):
    x = df.drop(columns=['Weekly_Sales'])
    y = df.Weekly_Sales
    return x,y

    

