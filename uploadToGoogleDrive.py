from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from oauth2client.service_account import ServiceAccountCredentials
import os
import csv
import time
from utils.GoogleDrivefunc import getGoogleService, uploadFileToGoogleDrive
from utils.InitialValue import KEYFILE, AUDIOSAVEDIR, AUDIOUPLOADDIRID, UPLOADLOGFILE
import datetime

keyFile = KEYFILE
dirname = AUDIOSAVEDIR
updirID = AUDIOUPLOADDIRID
UploadLogFile = UPLOADLOGFILE

# フォルダに録音データがないときに待つ時間
waitTime = 600

def main():
    #あとから値を代入する変数郡
    fileID = ""
    fileName = ""
    files = os.listdir(dirname)

    if len(files) > 0:
        files.sort()
        filepath = dirname + files[0]

        #getGoogleService(keyFile)
        fileID = uploadFileToGoogleDrive(files[0], filepath, updirID, keyFile)
        dt_now = datetime.datetime.now().strftime('%Y_%m_%d-%H_%M_%S')
        with open(UploadLogFile, 'a') as f:
            writer = csv.writer(f)
            writer.writerow([dt_now, files[0], fileID])
        os.remove(filepath)
    else :
        print("wait. don't find files")
        time.sleep(waitTime)



if __name__ == "__main__":
    while True:
        try:
            main()

        except KeyboardInterrupt:
            print("Ctrl+C finished")
            break

        except BrokenPipeError:
            print("BrokenPipeError")
            print("reconnect")

        except ConnectionResetError:
            print("ConnectionResetError")
            print("reconnect")

        except Exception as e:
            print("unexpected error")
            print(e)
