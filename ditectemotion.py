def ditectemotion(image_url):
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

    #write KEY in seacret.py
    ENDPOINT = "https://yattinda.cognitiveservices.azure.com/"

    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

    single_face_image_url = image_url
    single_image_name = os.path.basename(single_face_image_url)

    detected_faces = face_client.face.detect_with_url(url=single_face_image_url, detectionModel='detection_02', return_face_attributes=["emotion"])

    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))


    for face in detected_faces:
        return face.face_attributes.emotion)

    #return detected_faces

# if __name__ == '__main__':
#     main()
        # response = requests.get(single_face_image_url)
        # img = Image.open(BytesIO(response.content))
        #
        # print('Drawing rectangle around face... see popup for results.')
        # draw = ImageDraw.Draw(img)
        # for face in detected_faces:
        #     draw.rectangle(getRectangle(face), outline='red'
        #
        # img.show()
