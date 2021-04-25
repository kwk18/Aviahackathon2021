import boto3


session = boto3.Session()
s3_client = session.client(
    service_name='s3',
    endpoint_url='https://storage.yandexcloud.net'
)


def download_doc(name):
    key_name = 'consent_personal_data_JohnSmith.docx'
    s3_client.get_object(Bucket='www.documents.com', Key=key_name)
# for key in s3_client.list_objects(Bucket='www.documents.com')['Contents']:
#     print(key['Key'])
#
# file = s3_client.get_object(Bucket='www.documents.com', Key='figma-logo.png')
# with open('Вася Пупкин_sign.png', 'wb') as f:
#     f.write(file['Body'].read())


# if __name__ == "__main__":
#     temp_list = main.filling_and_uploading()
#     name_of_file = temp_list[0]
#     name_of_person = temp_list[1]
#     person_id = temp_list[2]
#     link = 'https://storage.yandexcloud.net/www.documents.com/docs_uploaded/' + name_of_file
#     s3_client.upload_file(name_of_file, 'www.documents.com', 'docs_uploaded/' + name_of_file)
#     f = open('../web/temp', 'w')
#     f.write(link)
#     f.close()
#     qr.generate("localhost:5050/?url=" + str(person_id))

