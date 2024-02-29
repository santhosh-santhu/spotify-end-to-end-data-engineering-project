# Spotify End-To-End Data Engineering Project

### Description
In these project,we will build an ETL(Extract,Transform,Load) pipeline using the Spotify API on AWS.The pipeline will retrieve data from the Spotify API,transform it to a desired format,and load it into an AWS data store.

### Architecture 
![Architecture Diagram](https://github.com/santhosh-santhu/spotify-end-to-end-data-engineering-project/blob/main/aws-data-Architecture.jpg)


### About Dataset/API 
This API contain information about music artist, albums and songs

### Services Used
1. **S3(Simple Storage Service):** Amazon S3 is a highly scalable object storage service that can store and retrieve any amount of data from anywhere on the web. It is commonly used to store and distribute large media files, data backups, and static website files.
2. **AWS Lambda:** AWS Lambda is a serverless computing service that lets you run code without managing servers.You can use Lambda to run code in response to events like changes in S3,DynamoDB, or other AWS services.
3. **Cloud Watch:** Amazon CloudWatch is a monitoring for AWS resources and the applications you run on them. You can use CloudWatch to collect and tracks metrics, collect and monitor log files, and set alarms.
4. **Glue Crawler:** AWS Glue Crawler is a fully managed service that automatically crawls your data sources,identifies data format, and infers schemas to create and AWS Glue Data catalog.
5. **Data Catalog:** AWS Glue Data Catalog is a fully managed metadata repository that makes it easy to discover and manage data in AWS. You can use the Glue Data Catalog with other AWS services, such as Athena
6. **Amazon Athena:** Amazon Athena is a interactive query service that makes it easy to analyze data in Amazon S3 using standard SQL.You can use Athena to analyze data in your Glue Data Catalog or in other S3 buckets.



### Install Packages
```
pip install pandas
pip install numpy
pip install spotipy
```
### Project Execution Flow 
Extract Data from API -> Lambda Trigger (every hour) -> Run Extract Code -> Store Raw Data -> Trigger Transform Function -> Transform Data and Load It -> Query Using Athena  
  
