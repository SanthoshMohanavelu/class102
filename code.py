import random
import cv2
import dropbox
import time

def capturePic():
    capturePicture = cv2.VideoCapture(0)
    result = True
    number = random.randint(0,100)
    while(result):
        ret, frame = capturePicture.read()
        imageName = "MyPic"+str(number)+".png"
        cv2.imwrite(imageName, frame)
        start_Time = time.time
        result = False 
    return imageName
    print("Image has been captured")
    capturePicture.release()
    capturePicture.destroyAllWindows()

def upload_file(imageName):
    access_token = 'sl.BF3LUWRZQQNDg99o1ZfXyQyinanr8765rqei1sOM1Ec2qbqP89nLCefvUUQLCaOkt9__ChG9hziMW3Zc5gWjAKuPjy0cDCP-PfL9GJK1YTzte6LUdj57_euWo3En_l33DwMvS4niez-z'
    file = imageName
    file_from = file
    file_to = "/TestPicFolder/" + (imageName)
    dbx = dropbox.Dropbox(access_token)
    with open(file_from, 'rb') as f: 
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")
def main():
    while(True):       
        name = capturePic()
        upload_file(name)


main()