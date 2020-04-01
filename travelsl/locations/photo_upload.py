from azure.storage.blob import BlockBlobService , ContentSettings
import uuid
import base64

def upload_file_to_azure(base_64_image):
    """
    image upload to azure blob storage
    :param base_64_image:
    :return:
    """
    image_name = str(uuid.uuid4())

    base64_img_bytes = base_64_image.replace("data:image/png;base64,","").encode('utf-8')
    blob_service_client = BlockBlobService("travelsl","xF0VCFJk6X3Nc+vUAz1sfraRzhj5gcg36BSurzHDOuu18YR/iEYnId/qxwyIpTksr0znuAV/F8Y4ExeGYBQtKw==")
    blob_service_client.create_blob_from_text("locationimages",image_name,base64.decodebytes(base64_img_bytes),encoding="base64",content_settings=ContentSettings(content_type="image/png",content_encoding="base64"))
    return "https://travelsl.blob.core.windows.net/locationimages/{}".format(image_name)
