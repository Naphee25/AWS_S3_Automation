import boto3


# Printing the list of buckets
def print_content(s3_client, region_name=None):
    if region_name:
        for bucket in s3_client.list_buckets()["Buckets"]:
            if s3_client.get_bucket_location(Bucket=bucket['Name'])['LocationConstraint'] == region_name:
                print(bucket["Name"])
    else:
        for bucket in s3_client.list_buckets()["Buckets"]:
            print(bucket["Name"])


# main program
if __name__ =="__main__":
    # accessing aws $3 service by creating an instance
    S3_client = boto3.client('s3')
    s3_resource = boto3. resource('s3')
    region_name = "eu-north-1"

    print_content (s3_client, region_name)

print("Program finished")