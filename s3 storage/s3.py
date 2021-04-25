import boto3

session = boto3.Session()
s3_client = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)

for key in s3_client.list_objects(Bucket='www.documents.com')['Contents']:
    print(key['Key'])

#получение объекта из storage
file = s3_client.get_object(Bucket='www.documents.com', Key='figma-logo.png')
with open('f.png', 'wb') as f:
    f.write(file['Body'].read())


s3_client.upload_file('ver.jpg', 'www.documents.com', 'uploaded/test-vera.jpg')

