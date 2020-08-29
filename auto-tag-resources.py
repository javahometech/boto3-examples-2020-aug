import boto3
import json

s3_client = boto3.client('s3')
ec2_client = boto3.client('ec2')

def lambda_handler(event,context):
    # get tag information from s3
    s3Resp = s3_client.get_object(
        Bucket='javahome-auto-tagging',
        Key='tags.json'
    )
    strData = s3Resp['Body'].read().decode("utf-8")
    dictData = json.loads(strData)
    # create a tag on ec2 instance.
    instance_id = event['detail']['responseElements']['instancesSet']['items'][0]['instanceId']
    ec2_client.create_tags(
        Resources = [instance_id],
        Tags = dictData['Tags']
    )

lambda_handler(None,None)   
