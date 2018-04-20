import pandas as pd
import datetime
# read data
def get_Merged(filename):
    df = pd.read_csv(filename)
    df = df.drop(columns=['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5','CPI','Unemployment'])
    df = df.drop(columns=['Dept'])
    return  df
# print(df)

# preprocess
def preprocess_type(df):
    df['TypeA'] = df['Type'].map({'A':1, 'B':0, 'C':0})
    df['TypeB'] = df['Type'].map({'A':0, 'B':1, 'C':0})
    df['TypeC'] = df['Type'].map({'A':0, 'B':0, 'C':1})

    df = df.drop(columns=['Type'])
    return df

def send_xy(df):
    x = df.drop(columns=['Weekly_Sales'])
    y = df.Weekly_Sales
    return x,y

def preprocess_date(df):
    df['date_weight'] = df['IsHoliday'].map({True:2, False:1})
    df = df.drop(columns=['IsHoliday', 'Date'])
    return df

def preprocess_test(filename):
    df = get_Merged(filename)
    df = preprocess_type(df)
    df = preprocess_date(df)
    return df

def send_submission(submit_filename, res):
    df_sample_submission = pd.read_csv('dataset/sampleSubmission.csv')
    df_sample_submission['Weekly_Sales'] = res
    df_sample_submission.to_csv(submit_filename, index=False)