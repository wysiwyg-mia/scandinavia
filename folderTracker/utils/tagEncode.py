import time
import datetime

def payload(ds):
    """ The function gets info from dicom file and decodes it. """
    data = []

    # fio
    fio = ds[0x0010, 0x0010]
    fioValue = fio.value
    # encoding fio
    fioEncoded = character(fioValue)
    # remove ^
    fio = fioEncoded.replace("^", " ")
    data.append(fio)

    # studyDate
    studyDateTemp = ds[0x0008, 0x0020]
    studyDateValue = studyDateTemp.value
    # formating date
    year = studyDateValue[:4]
    month = studyDateValue[4:6]
    day = studyDateValue[6:8]
    study = year + "-" + month + "-" + day

    studyTime = ds[0x0008, 0x0030]
    t = studyTime.value
    time = ':'.join(a+b for a,b in zip(t.split('.')[0][::2], t.split('.')[0][1::2]))
    data.append(study+ ' ' +time)

    # dob
    dob = ds[0x0010, 0x0030]
    dobValue = dob.value
    # formating date
    year = dobValue[:4]
    month = dobValue[4:6]
    day = dobValue[6:8]
    dobDate = year + "-" + month + "-" + day
    data.append(dobDate)

    # sex
    sex = ds[0x0010, 0x0040]
    sexValue = sex.value
    data.append(sexValue)

    #mobile phone number
    phone = ds[0x0010, 0x2154]
    phoneValue = phone.value
    #phone number has to contain only 11 numbers. For example "9171112233"
    if phoneValue[0] != "":
        if len(phoneValue[0]) == 11:
            phoneValue[0] = phoneValue[0][1 : : ]
        if len(phoneValue[0]) == 12:
            phoneValue[0] = phoneValue[0][2 : : ]
        data.append(phoneValue[0])
    else:
        if phoneValue[1] != "":
            if len(phoneValue[1]) == 11:
                phoneValue[1] = phoneValue[1][1 : : ]
            if len(phoneValue[1]) == 12:
                phoneValue[1] = phoneValue[1][2 : : ]
            data.append(phoneValue[1])
        else:
            data.append("")

    # address
    address = ds[0x0010, 0x1040]
    addressValue = address.value
    addressValue = " ".join(addressValue.split())
    #replace English with Russian
    if addressValue == 'City: Street: bldg: apt:':
        data.append('')
    else:
        addressEncoded = character(addressValue)
        for r in (("City:", "Город:"), ("Street","улица"),("bldg", "дом"), ("apt","квартира")):
            addressEncoded = addressEncoded.replace(*r)
        data.append(addressEncoded)
    address = ds[0x0010, 0x1040]
    addressValue = address.value
    # encoding address
    addressEncoded = character(addressValue)
    # formating address
    for r in (("City:", "Город:"), ("Street","улица"),("bldg", "дом"), ("apt","квартира")):
        addressEncoded = addressEncoded.replace(*r)
    data.append(addressEncoded)
    

    doc = ds[0x0008, 0x1060]
    docValue = doc.value
    docEncoded = character(docValue[0])

    
    data.append(docEncoded)
    
    return data

def character(string):
    """
        The function recieves string, decode it and returns new decoded string. 
    """
    temp = string.encode('ISO-8859-1')
    encoding = 'WINDOWS-1251'
    data = temp.decode(encoding)

    return data