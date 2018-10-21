import boto3
import io
import urllib
import json
import pprint
import base64
import uuid
from datetime import datetime
from decimal import Decimal

rekognition = boto3.client('rekognition', region_name='us-east-1')
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')




def lambda_handler(event, context):
    table = dynamodb.Table('emoData')
    
    try:
        #Take Input from API gateway and convert base64 in to byte blob
        imageString = event["body"].replace('data:image/jpeg;base64,','').replace('"',"")
        imgdata = base64.b64decode(imageString)
        
        #Index all faces in the image
        
        face_index = rekognition.index_faces(Image={"Bytes":imgdata},CollectionId="facedb",DetectionAttributes=['ALL'])
        for face in face_index["FaceRecords"]:
            print(json.dumps(face["FaceDetail"]))
        
            table.put_item(
                Item={
                   'datetime':datetime.utcnow().isoformat(),
                   'faceId':face["Face"]["FaceId"],
                   'ageLow': face["FaceDetail"]["AgeRange"]["Low"],
                   'ageHigh': face["FaceDetail"]["AgeRange"]["High"],
                   'smileValue': face["FaceDetail"]["Smile"]["Value"],
                   'smileConfidence': Decimal(face["FaceDetail"]["Smile"]["Confidence"]),
                   'gender':face["FaceDetail"]["Gender"]["Value"],
                   'genderConfidence':Decimal(face["FaceDetail"]["Gender"]["Confidence"]),
                   'eyesOpen':face["FaceDetail"]["EyesOpen"]["Value"],
                   'eyesOpenConfidence':Decimal(face["FaceDetail"]["EyesOpen"]["Confidence"]),
                   'emotionCALM':Decimal(face["FaceDetail"]["Emotions"][0]["Confidence"]),
                   'emotionSAD':Decimal(face["FaceDetail"]["Emotions"][1]["Confidence"]),
                   'emotionHAPPY':Decimal(face["FaceDetail"]["Emotions"][2]["Confidence"]),
                   "qualityBrightness":Decimal(face["FaceDetail"]["Quality"]["Brightness"]),
                   "qualitySharpness":Decimal(face["FaceDetail"]["Quality"]["Sharpness"])
                }
            )
        
        
        return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json",
            "errors": "none",
            "Access-Control-Allow-Origin" : '*',
            "test":"yes"
        },
        "body": "Success"
        }
        
    except Exception as e:
        return {
        "statusCode": 500,
        "headers": {
            "Content-Type": "application/json",
            "errors": str(e),
            "Access-Control-Allow-Origin" : '*',
            "test":"yes"
        },
        "body": "failure"
        }
        
       
        
    
        
