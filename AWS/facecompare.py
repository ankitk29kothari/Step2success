
import boto3


#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)



def compare_faces(sourceFile, targetFile):


    #Authentication
    client = boto3.client('rekognition',aws_access_key_id="",aws_secret_access_key="",region_name='ap-south-1')

   
    #convert file format
    imageSource=open(sourceFile,'rb')
    imageTarget=open(targetFile,'rb')

    #calling API
    response=client.compare_faces(SimilarityThreshold=80,
                                  SourceImage={'Bytes': imageSource.read()},
                                  TargetImage={'Bytes': imageTarget.read()})
    
    print(response)

###################################################
    for faceMatch in response['FaceMatches']:
        position = faceMatch['Face']['BoundingBox']
        similarity = str(faceMatch['Similarity'])
        print('The face at ' +
               str(position['Left']) + ' ' +
               str(position['Top']) +
               ' matches with ' + similarity + '% confidence')

    imageSource.close()
    imageTarget.close()     
    return len(response['FaceMatches'])          

def main():
    
    import time
    t1=time.perf_counter()
    source_file='photo1.jpg'
    #target_file='aws.jpg'
    target2_file='photo2.jpg'

    face_matches=compare_faces(source_file, target_file)
    print("Face matches: " + str(face_matches))

    face_matches=compare_faces(source_file, target2_file)
    print("Face matches: " + str(face_matches))
    t2=time.perf_counter()
    print(t2-t1)


if __name__ == "__main__":
    main()