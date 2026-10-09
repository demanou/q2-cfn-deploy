import boto3

s3 = boto3.client("s3")

message = "Hello from AWS Glue!"
print(message)

s3.put_object(
    Bucket="dnag-s3-demo-bucket",
    Key="glue-output/hello.txt",
    Body=message
)
