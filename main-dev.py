import sys
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from subprocess import Popen

class ReloadHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.restart_program()

    def restart_program(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        self.process = Popen([sys.executable, self.script])

    def on_modified(self, event):
        _, ext = os.path.splitext(event.src_path)
        if ext in ['.py', '.ui', '.qrc']:
            print(f"📝 Arquivo modificado: {event.src_path}. Reiniciando...")
            self.restart_program()

if __name__ == "__main__":
    script_name = "main-prod.py" 
    path = "."  

    event_handler = ReloadHandler(script_name)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("👀 Monitorando mudanças...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
