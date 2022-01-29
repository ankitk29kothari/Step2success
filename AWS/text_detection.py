import boto3

def detect_text(photo, bucket):

    client = boto3.client('rekognition',aws_access_key_id="",aws_secret_access_key="",region_name='ap-south-1')

    Image=open(photo,'rb')

    response=client.detect_text(Image={'Bytes': Image.read()})
                        
    textDetections=response['TextDetections']
    print ('Detected text\n----------')
    for text in textDetections:
            print (text['DetectedText'])
            #print ('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            #print ('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                #print ('Parent Id: {}'.format(text['ParentId']))
                pass
            #print ('Type:' + text['Type'])
            print()
    return len(textDetections)

def main():

    bucket=''
    photo='reviews.png'
    text_count=detect_text(photo,bucket)
    print("Text detected: " + str(text_count))


if __name__ == "__main__":
    main()