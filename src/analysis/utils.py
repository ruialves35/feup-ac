import pandas as pd
from sklearn.linear_model import LinearRegression
from category_encoders.cat_boost import CatBoostEncoder

## Function to calculate the linear regression
## and imput the missing values
def predictColumnLR(df, column, columns = ['num_inhabitants', 'municip499', 'municip500_1999', 'municip2000_9999', 'municip10000', 'num_cities',
        'urban_ratio', 'avg_salary', 'unemp_rate95', 'unemp_rate96', 'num_entrepreneurs', 'num_crimes95', 'num_crimes96',
        'num_crimes95_ratio']):
    # select only num_inhabitants and municip499 columns
    lr = LinearRegression()
    no_val_df = df[df[column].isnull() == True]
    val_df = df[df[column].isnull() == False]

    df = df[columns]
    droplist = [col for col in df.columns if col != column and df[col].isnull().values.any()]
    df.drop(droplist,axis=1,inplace=True)

    testdf = df[df[column].isnull() == True]
    traindf = df[df[column].isnull() == False]

    y = traindf[column]
    traindf.drop(column, axis=1, inplace=True)
    lr.fit(traindf ,y)
    testdf.drop(column, axis=1, inplace=True)
    no_val_df.drop(column, axis=1, inplace=True)

    pred = lr.predict(testdf)
    print(column, " predictions = ", pred)
    no_val_df[column] = pred

    return pd.concat([val_df, no_val_df])


# Transform the categorical columns into numerical values using CatBoostEncoder
def cat_boost_encode(df, cols, df_test):
    target = df['paid']
    df.drop(['paid'], axis='columns', inplace=True)
    encoder = CatBoostEncoder(cols=cols)

    encoder.fit(df, target)
    df = encoder.transform(df)
    df['paid'] = target

    curr_paid = df_test['paid']
    df_test.drop(['paid'], axis='columns', inplace=True)
    df_test = encoder.transform(df_test)
    df_test['paid'] = curr_paid

    return (df, df_test)
   

# Do one hot encoding on cols of data frame
def one_hot_encode(df, cols):
  df = pd.get_dummies(df, columns=cols)
  return df
