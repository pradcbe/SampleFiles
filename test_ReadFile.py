import boto3
from moto import mock_s3
from Code.ReadFile import lambda_GetFileNames

sbucketName = "AIGBUCKET"
sfileName = "SampleFile.txt"
sBody = "AIG Sample File"

def test_lambda_get_file_names():
    set_up_s3()
    event = {
        "BucketName": sbucketName
    }
    result = lambda_GetFileNames(event, None)
    assert result == {"files": [{"filename": "SampleFile.txt"}]}

def set_up_s3():
    with mock_s3():
        # Create the bucket & write the object
        s3 = boto3.resource('s3', region_name='us-east-1')
        s3.create_bucket(Bucket=sbucketName)
        s3.Object(bucket_name=sbucketName, key=sfileName)
