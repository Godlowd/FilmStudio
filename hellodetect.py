import boto3

def detect(bucket , name):
    rekognition = boto3.client("rekognition")
    print("this is the bucket{bucket}")
    
    
detect("foo","bar")