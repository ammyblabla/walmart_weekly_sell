import pandas as pd
# read data
def get_Merged(filename):
    df = pd.read_csv(filename)
    df = df.drop(columns=['MarkDown1','MarkDown2','MarkDown3','MarkDown4','MarkDown5','CPI','Unemployment'])
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

def preprocess_date(df, is_return_date_holiday=False):
    sale_date = df.Date
    IsHoliday = df.IsHoliday
    df = df.drop(columns=['Date', 'IsHoliday'])
    if is_return_date_holiday:
        return df, sale_date, IsHoliday  
    else:
        return df

def preprocess_train(filename, is_return_date_holiday=False):
    df = get_Merged(filename)
    df = preprocess_type(df)
    df, date, holiday = preprocess_date(df,True)
    x,y = send_xy(df)
    if is_return_date_holiday:
        return df, x, y, date, holiday
    return df, x, y

def preprocess_test(filename):
    df = get_Merged(filename)
    df = preprocess_type(df)
    df = preprocess_date(df)
    # x,y = send_xy(df)
    # if is_return_date_holiday:
    #     return df, x, y, date, holiday
    return df

def send_submission(submit_filename):
    df_sample_submission = pd.read_csv('dataset/sampleSubmission.csv')
    df_sample_submission['Weekly_Sales'] = res
    df.to_csv(submit_filename, index=False)