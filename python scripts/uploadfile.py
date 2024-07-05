local_file_path = input("Drag and drop file to terminal then rtn: ")
import datetime, os
from dotenv import load_dotenv

load_dotenv()

b2_file_name = local_file_path.split("\\")[-1]

provider = input("Which Cloud provider should this file be uploaded to?\n\
                 > 0: Backblaze B2\n\
                 > 1: [S3 Compatible provider of your choice]\n\
                 Select> ")

isTemp = 0

if provider == "0":

    #backblaze specific

    import b2sdk.v2 as b2

    info = b2.InMemoryAccountInfo()
    b2_api = b2.B2Api(info)
    application_key_id = os.getenv("B2_APPLICATION_KEY_ID")
    application_key = os.getenv("B2_APPLICATION_KEY")
    b2_api.authorize_account("production", application_key_id, application_key)

    bucket_name = os.getenv("B2_BUCKET_NAME")
    bucket = b2_api.get_bucket_by_name(bucket_name)

    file_info = bucket.upload_local_file(local_file=local_file_path, file_name=b2_file_name)
    print(file_info)

    fileURL = os.getenv("B2_FILE_URL_PREFIX")+b2_file_name

elif provider == "1":

    #Any S3 compatible (R2, S3, etc.)

    import boto3

    s3 = boto3.resource(
        "s3",
        endpoint_url=os.getenv("S3_COMPAT_ENDPOINT_URL"),
        aws_access_key_id=os.getenv("S3_COMPAT_ACCESS_KEY_ID"),
        aws_secret_access_key=os.getenv("S3_COMPAT_SECRET_ACCESS_KEY"),
    )

    # Specify the bucket and file
    bucket = s3.Bucket(os.getenv("S3_COMPAT_BUCKET_NAME"))

    #This part requires you to set up prefix lifecycle rules in your S3 provider!

    lifecycle = input("Setting file validity period.\n\
                      > 0: 7 days (default)\n\
                      > 1: 30 days\n\
                      > 2: No expire date\n\
                      Select> ")

    if lifecycle == "0" or lifecycle == "":
        prefix = "week/"
        isTemp = 1
    elif lifecycle == "1":
        prefix = "month/"
        isTemp = 2
    elif lifecycle == "2":
        prefix = ""
    else:
        print("please enter valid lifecycle")
        exit
    with open(local_file_path, "rb") as f:
        res = bucket.Object(prefix+b2_file_name).put(Body=f.read())

    fileURL = os.getenv("S3_COMPAT_FILE_URL_PREFIX")+prefix+b2_file_name

# This is "extensible", just use seperate if statements for different providers with the dotenv file

print("file uploaded with link at " + fileURL)

ans = input("rtn to end script, 1 to shorten with Short.io settings, and something else to shorten with a slug of your choice: ")



if ans != "":    

    short_io_api_key = os.getenv("SHORT_IO_API_KEY")

    import requests

    url = "https://api.short.io/links"

    payload = {
        "domain": os.getenv("SHORT_IO_DOMAIN"),
        "originalURL": fileURL,
    }

    if ans != "1":
        payload["path"] = ans

    #You may have to change the numbers based on how you set up the lifecycle rules

    if isTemp == 1:
        oneWeekSec = datetime.datetime.now() + datetime.timedelta(weeks=1)
        payload["ttl"] = int(oneWeekSec.timestamp() * 1000) + 100000

    elif isTemp == 2:
        WeekSec = datetime.datetime.now() + datetime.timedelta(weeks=4)
        payload["ttl"] = int(WeekSec.timestamp() * 1000) + 100000

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": short_io_api_key
    }

    response = requests.post(url, json=payload, headers=headers)

    if response.status_code == 200:
        print("Shortened URL:", response.json()["shortURL"])
        input("press enter to close!")
    else:
        print("Error:", response.json())
        input("press enter to close!")