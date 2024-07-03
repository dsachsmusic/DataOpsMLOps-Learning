#Run the following: Note that the exclaimation point is so we can run shell commands from within Jupyter notebook
# !pip install --upgrade s3fs #this is because, as of writing, default python s3fs library is old(?) after running this, restart kernel

import sagemaker #used for interacting with the sagemaker tool in various ways(?)
import boto3 #python sdk of interacting with AWS S3 buckets and such(?)
import pandas as pd #pandas, for data manipulation, I think. 
from sagemaker import get_execution_role #get_execution_role function is used to retreve the IAM role...that is configured (was configured earlier?) for use with this notebook...to access S3 buckets, etc?

import scikit-learn #a.k.a scikit-learn - python library with lots of features....contains the functionality for  Logistic Regression, etc.
Regression: Linear Regression, Ridge Regression, Lasso Regression, etc.
Clustering: 
from sklearn.model_selection import train_test_split #functionality for splitting dataset into two subsets: one for training your model and one for testing it.
from sklearn.linear_model import LinearRegression #this contains the functionality to train a model to predict based on correlation...it works to understand the data determine the most appropiate correlation coefficients for accurate prediction...line of best fit, etc (that stuff (?))
from sklearn.metrics import mean_squared_error #for testing how well the model predicts...(MSE is a single floating-point number representing the average squared difference between y_true and y_pred.(?))

# the data (preped using Amazon Glue Codebrew, earlier)
s3_bucket = "webs1te"
s3_prefix = 'gluebrew-cleaned-data-hello-housing_03Jul2024_1719974783108/gluebrew-cleaned-data-hello-housing_03Jul2024_1719974783108_part00000.csv'
s3_input = f's3://{s3_bucket}/{s3_prefix}'
print(s3_input)

df = pd.read_csv(s3_input) #create/import(?) the dataframe in/with pandas
df.head() #print out the first rows - to look to import/confirm it looks good (?)

from sklearn.model_selection import train_test_split

train, test = train_test_split(df, test_size=0.2)
train.to_csv('train.csv', index=False)
test.to_csv('test.csv', index=False)

s3_train_path = f's3://{s3_bucket}/train/train.csv'
s3_test_path = f's3://{s3_bucket}/test/test.csv'

# Upload the training and test data to S3
boto3.Session().resource('s3').Bucket(s3_bucket).Object('train/train.csv').upload_file('train.csv')
boto3.Session().resource('s3').Bucket(s3_bucket).Object('test/test.csv').upload_file('test.csv')


#whats next?