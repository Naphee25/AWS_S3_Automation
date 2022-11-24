import boto3
import logging
from botocore.exceptions import ClientError
import time


# a file to upload to a bucket
def upload_file(s3_resource, bucket_name, file_path, file_name):
    try:
        data = open(file_path, 'rb')
        start = time.time()
        s3_resource.Bucket(bucket_name).put_object(Key=file_name, Body=data)
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

    # print (upload_f1le(boto3.resource('s3'), bucket_name,". /images/CDN-1.PNG", "CDN-1.PNG"))

print("Uploading time")
print("1MB   -- ", upload_file(s3_resource, bucket_name, "./files/1MB.text", "1MB.text"))
print("10MB  -- ", upload_file(s3_resource, bucket_name, "./files/10MB.text", "10MB.text"))
print("100MB -- ", upload_file(s3_resource, bucket_name, "./files/100MB.text", "100MB.text"))
print("500MB -- ", upload_file(s3_resource, bucket_name, "./files/500MB.text", "500MB.text"))

print("Program finished")