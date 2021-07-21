import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
# import fileReader
import pydicom

class CrtHandler(PatternMatchingEventHandler):
    patterns = ["*.dcm"]

    def on_created(self, event):
        self.process(event)
        ds = pydicom.dcmread(event.src_path, force=True)
        info = fileReader.getInfo(ds, event.src_path)

if __name__ == '__main__':
    path = '/Users/user/dev/mpc/folderTracker/uploads/'

    observer = Observer()
    observer.schedule(CrtHandler(), path=path)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()