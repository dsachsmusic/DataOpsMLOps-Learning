############################
##  universal variables   ##
############################
# the data (originally preped, very lightly...i.e. removed some nulls, using Amazon Glue Codebrew, earlier)
s3_bucket = "webs1te"
s3_path_housing_data = 'gluebrew-cleaned-data-hello-housing_03Jul2024_1719974783108/gluebrew-cleaned-data-hello-housing_03Jul2024_1719974783108_part00000.csv'
s3_input = f's3://{s3_bucket}/{s3_path_housing_data}'
print(s3_input)

# parameter for limiting data to process, so we don't spend to much during development
nrows_to_read = 1000
############################
## Use linear regression  ## note!!!!!!
############################

import pandas as pd #pandas, for data manipulation, I think. 
import sklearn #a.k.a scikit-learn - python library with lots of features....contains the functionality for  Logistic Regression, etc.

from sklearn.model_selection import train_test_split #functionality for splitting dataset into two subsets: one for training your model and one for testing it.
from sklearn.linear_model import LinearRegression #this contains the functionality to train a model to predict based on correlation...it works to understand the data determine the most appropiate correlation coefficients for accurate prediction...line of best fit, etc (that stuff (?))
from sklearn.metrics import mean_squared_error #for testing how well the model predicts...(MSE is a single floating-point number representing the average squared difference between y_true and y_pred.(?))


from sklearn.preprocessing import OneHotEncoder #oneHotEncoder, for encoding categorical data, as binary vectors, so that we can use those as features ...because machine learning doesn't do well with categorical data
from sklearn.preprocessing import StandardScaler #to transformed features' data to have a mean of 0 and a standard deviation of 1 (by subtracting feature's mean value from each data point, and dividing each feature's datapoints by features standard deviation). not sure if crucial here.
from sklearn.compose import ColumnTransformer #for (specifying which to features ...i.e. columns... to apply which to, and) applying the OneHotEncoder and StandardScalar transforms to the features
from sklearn.pipeline import Pipeline #for processing the data through the various steps (transforms first, then ML algorithm)

data = pd.read_csv(s3_input, nrows=nrows_to_read) #create/import(?) the dataframe in/with pandas
data.head() #print out the first rows - to look to import/confirm it looks good (?) #

data = data.dropna() #remove nulls

# Extract features and target variable ...in supervised learning (what we are doing) you have features and a target...typically represented by x and y(?)
X = data[['bed', 'bath', 'acre_lot', 'house_size', 'city', 'state', 'zip_code']]
y = data['price']


# Encode categorical features
categorical_features = ['city', 'state', 'zip_code']
numerical_features = ['bed', 'bath', 'acre_lot', 'house_size']

# Preprocessing pipeline for numerical and categorical features
# Note: handle_unknown=ignore makes it so any novel(?) categorical data values (values that were not present in the training data, are ignored, when this preprocessor is used)
preprocessor = ColumnTransformer(
    transformers=[
        ('num', StandardScaler(), numerical_features),    # Scale numerical features
        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)     # One-hot encode categorical features.      
        
    ],
    remainder='passthrough'  # Keep any remaining columns unchanged
)

# Define the model pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('model', LinearRegression())
    
])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Train the model
pipeline.fit(X_train, y_train)

# Make predictions

X_test_encoded = preprocessor.transform(X_test) #for testing, encode the test data with onehot encoding - because that is how the data was when we trained the data
#...but keep in mind, novel(?) values of categorical data will be ignored...because we used (handle_unknown='ignore) in the preprocessor...may be a better way to do it than this, but not sure
y_pred = pipeline.predict(X_test)

# Selecting a single row as a DataFrame
specific_row = X_test.loc[[803]]

# Making predictions
y_pred = pipeline.predict(specific_row)

# Actual value from y_test
actual_value = y_test.loc[803]

# Make predictions on the entire test set
y_pred = pipeline.predict(X_test)

# Create a DataFrame to compare actual vs. predicted values
comparison_df = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})

# Display the comparison DataFrame
print(comparison_df) 


# Compute MSE ...to evaluate how well model predicts

mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
############################
## Use XGBoost algorithm ##  ###not tested yet...also, might be costly.
############################

#notes: 
# XGBoost is a gradient boosting algorithm.
#  - can find non-linear relationships
#  - requires tuning several hyperparameters for optimal performance, such as
#  - we'll need a container...#  - unlike with scikit learns linear regression, where everything can be run within jupyter notebook, via Python...

#Run the following: Note that the exclaimation point is so we can run shell commands from within Jupyter notebook
# !pip install --upgrade s3fs #this is because, as of writing, default python s3fs library is old(?) after running this, restart kernel

import sagemaker #used for interacting with the sagemaker tool in various ways(?)
import boto3 #python sdk of interacting with AWS S3 buckets and such(?)
import pandas as pd #pandas, for data manipulation, I think. 
from sagemaker import get_execution_role #get_execution_role function is used to retreve the IAM role...that is configured (was configured earlier?) for use with this notebook...to access S3 buckets, etc?

#the IAM role set up previously, when setting up sagemaker (?)
role = get_execution_role()


data = pd.read_csv(s3_input, nrows=nrows_to_read) #create/import(?) the dataframe in/with pandas
data = data.dropna() #remove nulls

# One-Hot Encoding
data_encoded = pd.get_dummies(data, columns=['city', 'state', 'zip_code']) #this creates a column for each 

# Display the first few rows of the encoded data
print(data_encoded.head())

# Define features (X) and target (y) ... #note: while, when using sklearn linear regression, we pass x and y (feaures, target)...
# ...when using xgboost, our dataset implicitly indicates target, by following the convention of having the final column of the dataset be the target
X = data_encoded.drop(['price'], axis=1)  # All columns except 'price'
y = data_encoded['price']

# Combine features and target
data_combined = pd.concat([X, y], axis=1)

# Save to CSV, locally
data_combined.to_csv('house_listings_encoded.csv', index=False)

# Upload to S3 ....we have to do this so we the container can import it
import boto3

s3_housing_data_path = "house_data_modeling"

s3 = boto3.client('s3')

s3.upload_file('house_listings_encoded.csv', s3_bucket, s3_housing_data_path + '/house_listings_encoded.csv')  #parameters are local file, s3 bucket name, name to use when storing file in s3 bucket



train, test = train_test_split(data, test_size=0.2) 
train.to_csv('train.csv', index=False)
test.to_csv('test.csv', index=False)


s3_train_path = f's3://{s3_bucket}/{s3_housing_data_path}/train/train.csv'
s3_test_path = f's3://{s3_bucket}/{s3_housing_data_path}/test/test.csv'

# Upload the training and test data to S3
boto3.Session().resource('s3').Bucket(s3_bucket).Object(s3_housing_data_path + 'train/train.csv').upload_file('train.csv')
boto3.Session().resource('s3').Bucket(s3_bucket).Object(s3_housing_data_path + 'test/test.csv').upload_file('test.csv')


#The Docker image URI for XGBoost.
container = sagemaker.image_uris.retrieve('xgboost', boto3.Session().region_name, 'latest')

#estimator configures the training job.
xgb = Estimator(container, 
                role, 
                instance_count=1,
                instance_type='ml.t2.medium',  # Cost-effective for testing ....could also use spot instances to save more money
                output_path=f's3://{s3_bucket}//{s3_housing_data_path}/output', #where we'll save model artifacts - I guess this is needed because we are using a container that will spin down(?)
                sagemaker_session=sagemaker.Session())


xgb.set_hyperparameters(objective='multi:softmax',
                        num_class=3,
                        num_round=100)


s3_input_train = sagemaker.inputs.TrainingInput(s3_data=s3_train_path, content_type='csv')
s3_input_test = sagemaker.inputs.TrainingInput(s3_data=s3_test_path, content_type='csv')

xgb.fit({'train': s3_input_train, 'validation': s3_input_test})

# deploy the model
predictor = xgb.deploy(initial_instance_count=1, instance_type='ml.t2.medium')

# Read test data from S3 (assuming it's stored similarly to training data)
test_data = pd.read_csv(s3_path_housing_data)

# Remove any target column if present (if you have one)
test_data = test_data.drop(columns=['target_column_name'])

# Convert the test data to a suitable format (if necessary)
# For XGBoost, typically you would convert your features into a numpy array or pandas DataFrame

# Make predictions using the deployed endpoint
predictions = predictor.predict(test_data.values)

# Print or use predictions as needed
print(predictions)

# Delete the endpoint when done
predictor.delete_endpoint()