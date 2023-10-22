# Keep this script here for now. Will delete it later.
# Cheers, Cody!

from azure.storage.blob import BlobServiceClient
import sys

storage_account_key = "5HP4HoRNk0iezDenRwm3vKhjLIxNblXICn4oPSrefQsmHNjdoZiX8D/LH5hwTkj0rMJH3YI4FPYt+ASta0t/Mw=="
storage_account_name = "secretbootloader"
connection_string = "DefaultEndpointsProtocol=https;AccountName=secretbootloader;AccountKey=5HP4HoRNk0iezDenRwm3vKhjLIxNblXICn4oPSrefQsmHNjdoZiX8D/LH5hwTkj0rMJH3YI4FPYt+ASta0t/Mw==;EndpointSuffix=core.windows.net"
container_name = "secret"

if len(sys) < 2:
    print("Usage:"\n)
    print("python pyAz.py read")
    print("python pyAz.py upload {file_to_upload}")
    sys.exit(0)

blob_service_client = BlobServiceClient.from_connection_string(connection_string)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

def readFromBlobStorage():
    try:
        fetch_list = blob_service_client.get_container_client(container_name).list_blobs()
        for element in fetch_list:
            print(element.name)
    except Exception as e:
        print("Problem with fetching the blob list ! ", e)

def uploadToBlobStorage(file_path, file_name):
    try:
        with open(file_path, "rb") as file :
            blob_client.upload_blob(file)

        print(f"You just uploaded {file_name} to {container_name} !")
    except Exception as e:
        print("Problem with uploading to the blob storage!", e)
if sys.argv[1] == "read":
    readFromBlobStorage()

