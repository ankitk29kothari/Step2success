import boto3
photo='aws.jpg'

client = boto3.client('rekognition',aws_access_key_id="",aws_secret_access_key="",region_name='ap-south-1')

with open(photo,'rb')as source_image:
	source_bytes=source_image.read()

response= client.detect_faces(Image={'Bytes':source_bytes},Attributes=['ALL'])
a=(response['FaceDetails'])
#print(a)




for z in a:
	for k,v in z.items():
		print(k,v,'\n')
		if k=='Emotions':
			break
#for i in a:
#	print(i["Name"]," Confidence :",i['Confidence'])
