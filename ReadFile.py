## import the namespace
import boto3
import json

## define & assign variables
s3 = boto3.resource('s3', region_name='us-east-1')
data = {}
data['files'] = []

##lambda function to create the output. For example { “files”: [{ “name”: “file1”}, {“name”: “file2”},…]}
def lambda_GetFileNames(event, context):
    ## sBucketName = "clientmay2020"
    sBucketName = event["BucketName"]
    sBucket = s3.Bucket(sBucketName)
    listObjects = iter(sBucket.objects.all())
    ## iterate and get the key names in S3 bucket
    while True:
        try:
           skey = listObjects.__next__().key
           data['files'].append({'filename': skey})
        except:
            break

    json_str = json.dumps(data)
    return json_str

