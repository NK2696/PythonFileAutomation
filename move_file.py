from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


class MyHandler(FileSystemEventHandler):
    i = 1
    print('inside class')
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            src = folder_to_track + '/'+ filename
            new_destination = folder_destination + '/' + filename 
            print("src folder",src)
            os.rename(src, new_destination)

folder_to_track = 'E:/projects/move_file_automation/old_location'
folder_destination = 'E:/projects/move_file_automation/new_location'

event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()