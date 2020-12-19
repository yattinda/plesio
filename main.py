def main():
    # <snippet_imports>
    import asyncio
    import io
    import glob
    import os
    import sys
    import time
    import uuid
    import requests
    import seacret
    from urllib.parse import urlparse
    from io import BytesIO
    # To install this module, run:
    # python -m pip install Pillow
    #from PIL import Image, ImageDraw
    from azure.cognitiveservices.vision.face import FaceClient
    from msrest.authentication import CognitiveServicesCredentials
    from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person
    # </snippet_imports>
    # KEY = "f02503bf203a47ed95629b02c3e7f936"
    #write KEY in seacret.py
    ENDPOINT = "https://yattinda.cognitiveservices.azure.com/"
    IMAGE_BASE = "https://www.pakutaso.com/shared/img/thumb/MS251_imayaraduituyaru_TP_V.jpg"

    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    single_face_image_url = 'https://publicdomainq.net/images/202012/16s/publicdomainq-0051317.jpg'
    single_image_name = os.path.basename(single_face_image_url)

    detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detectionModel='detection_02', return_face_attributes=["emotion"])

    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))


    for face in detected_faces:
        print(face.face_attributes.emotion)

    #return detected_faces

if __name__ == '__main__':
    main()
        # response = requests.get(single_face_image_url)
        # img = Image.open(BytesIO(response.content))
        #
        # print('Drawing rectangle around face... see popup for results.')
        # draw = ImageDraw.Draw(img)
        # for face in detected_faces:
        #     draw.rectangle(getRectangle(face), outline='red'
        #
        # img.show()
