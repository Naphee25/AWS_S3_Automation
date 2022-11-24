import boto3
import logging
from botocore.exceptions import ClientError
import time


# delete a file from a bucket
def delete_file(s3_resource, bucket_name, file_name):
    try:
        s3_resource.Object(bucket_name, file_name).delete()

    except ClientError as e:
        print(e)
        logging.error(e)
        return False

    return True

# main program
if __name__ == "__main__":
    # accessing aws $3 service by creating an instance
    S3_client = boto3.client('s3')
    s3_resource = boto3. resource('s3')
    bucket_name = "Longnafisah-bucket-2"


delete_file(ss_resource, bucket_name, "CDN-1.PNG")

print("Program finished")