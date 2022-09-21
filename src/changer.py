import os
import time
import datetime
import filedate
import os, win32con, win32file, pywintypes


def changeCreationTime(path, time):
    try:
        wintime = pywintypes.Time(time)
        # File
        if os.path.isfile(path):
            winfile = win32file.CreateFile(path,
                                           win32con.GENERIC_WRITE,
                                           win32con.FILE_SHARE_READ |
                                           win32con.FILE_SHARE_WRITE |
                                           win32con.FILE_SHARE_DELETE,
                                           None,
                                           win32con.OPEN_EXISTING,
                                           win32con.FILE_ATTRIBUTE_NORMAL,
                                           None)
            win32file.SetFileTime(winfile, wintime, wintime, wintime)
            winfile.close()
            print(f'File {path} modified')
        # Directory
        elif os.path.isdir(path):
            windir = win32file.CreateFile(path,
                                          win32con.GENERIC_WRITE,
                                          win32con.FILE_SHARE_WRITE |
                                          win32con.FILE_SHARE_DELETE |
                                          win32con.FILE_SHARE_READ,
                                          None,
                                          win32con.OPEN_EXISTING,
                                          win32con.FILE_FLAG_BACKUP_SEMANTICS,
                                          None)
            win32file.SetFileTime(windir, wintime, wintime, wintime)
            windir.close()
            print(f"Directory {path} modified")
    except BaseException as err:
        print(err)


# Enter Folder path here!!
root = r"H:/"

year = 2022
month = 9
day = 10
hour = 18
minute = 30
second = 0

date = datetime.datetime(year=year, month=month, day=day, hour=hour, minute=minute, second=second)

for path, subdirs, files in os.walk(root):
    print(path + '\n\n')
    changeCreationTime(path, date)

    for name in files:
        fl = os.path.join(path, name)
        print(fl)
        changeCreationTime(fl, date)
