import boto3
import logging
from botocore.exceptions import ClientError
import time


# function to download a file from a bucket
def download_file(s3_client, bucket_name, file_name):
    try:
        start = time.time()
        s3_client.download_file(bucket_name, file_name, file_name)
        end = time.time()

    except ClientError as e:
        print(e)
        logging.error(e)
        return 0

    return end - start


# main program
if __name__ =="__main__":
    # accessing aws $3 service by creating an instance
    S3_client = boto3.client('s3')
    s3_resource = boto3. resource('s3')
    bucket_name = "Longnafisah-bucket-2"

print("Downloading time")
print("1MB   -- ", download_file(s3_client, bucket_name, "1MB.text"))
print("10MB  -- ", download_file(s3_client, bucket_name, "10MB.text"))
print("100MB -- ", download_file(s3_client, bucket_name, "100MB.text"))
print("500MB -- ", download_file(s3_client, bucket_name, "500MB.text"))