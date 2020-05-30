import boto3
photo='photo1.jpg'

client = boto3.client('rekognition',aws_access_key_id="AKIAQSEWML5GJXRGB2I3",aws_secret_access_key="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",region_name='ap-south-1')

with open(photo,'rb')as source_image:
	source_bytes=source_image.read()

response= client.detect_labels(Image={'Bytes':source_bytes}, MaxLabels=20)
a=(response['Labels'])
for i in a:
	print(i["Name"]," Confidence :",i['Confidence'])
