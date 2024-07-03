# Use AWS Glue DataBrew, for a visual and user-friendly environment for data preparation, (similar to Dataiku)
## Get data, in some way 
Get Data from AWS Data Exchange
- AWS Data Exchange > find a dataset ...subscribe to it
- AWS Data Exchange > Subscriptions > the dataset 
Configure to export to an S3 bucket
- To monitor export job: AWS Data Exchange > My Data > Entitled Data

Get data from external source...example
- Download data, such as https://www.kaggle.com/datasets/ahmedshahriarsakib/usa-real-estate-dataset 
- Go to S3 - upload the data (to a bucket)

## Create the dataset in AWS Glue Databrew
- AWS Glue Databrew > Datasets > Amazon S3 > select the file
...create Dataset
- AWS Glue Databrew > Projects ... create a new project with the dataset
 - For permissions, create a new role(?) IAM_AWSGlueDataBrew-Helloworld
- Note: When you create the project, a session starts.  Sessions are measured in 30 minute increments. Each session costs a dollar. It times out with no click/use. First 40 sessions are free for new users. 

## Prepare data (recipes) and transform 
- Create recipe - with steps (transforms)
- Create and run a job to apply steps to data/export results (to, for example, S3 bucket)
-- Note $0.48 per DataBrew node hour, default is 5 nodes

## Cleanup
- Delete anything in s3 not needed, to save money.
- or move to less expensive storage...note to self: https://drive.google.com/file/d/1Sgl7R_sb3ZDs7u6dcPdTvK9RUKn6v1az/view?usp=sharing

## Next steps 
- Import into AWS Sagemaker and do some ML?
- Try something similar in AWS Glue, and then do the Sagemaker thing

 