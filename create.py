import boto3
import logging
from botocore.exceptions import ClientError
import time


# func to create a bucket
def create_bucket(s3_resource, bucket_name, region=None):
    try:
        if region is None:
            s3_resource.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3_resource.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)

    except ClientError as e:
        print(e)
        logging.error(e)
        return False

    return True


# main program
if __name__ == "__main__":
    # accessing aws $3 service by creating an instance
    S3_client = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    region_name = "eu-north-1"

create_bucket("Longnafisah-bucket1", "ca-central-1")
create_bucket("Longnafisah-bucket2",  "eu-north-1")
create_bucket("Longnafisah-bucket3",  "ap-northeast-1")

print("Program finished")