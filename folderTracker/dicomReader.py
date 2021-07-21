import pydicom
import os
# import db
import json
# from sender import Req
# from remove import remove
import cv2


def getInfo(ds, path):
    """ 
        Function receives two args dataset and path to the file. 
        Function read and parse DICOM files using pydicom.
        More info about pydicom https://pydicom.github.io/pydicom/stable/old/ref_guide.html
    """
    # Check if file contains diagnoses.
    try:
        admittingDiagnoses = ds[0x0008, 0x1080]
        tempDiagnoses = admittingDiagnoses.value
        if '' in tempDiagnoses:
            return json.dumps({"data":[], "message": "Diagnoses tag can't be empty"})
    except Exception as e:
        return json.dumps({"data":[], "message": str(e)})

    diagnoses = []
    for item in enumerate(tempDiagnoses):
        diagnosesValueEncoded = db.character(item)
        # diagnoses.append(diagnosesValueEncoded)


    # data = db.payload(ds)
    # data.append(diagnoses[0])
    # # make a request
    # try:
    #     textPathOne = createPng(ds, path)
    #     # pass
    #     data.append(textPathOne)
    #     # print(data)
    #     info = Req.req(data)
    #     if not info:
    #         print("Error")
    #         return True
    #     remove(path)
    #     return True
    #     # Req.slackNotificationSuccess(info[1])
    # except Exception as e:
    #     print(ds)
    #     return False