import time
import io
import threading
import config as cfg

import cv2
        
def init_camera():
    try:
        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
        camera.set(cv2.CAP_PROP_FPS, 15)

        # camera setup
        #_,cls.frame = c.read()

        #cls.frame = cv2.resize(cls.frame, (320,240))
    
        
        return True, camera
    except:
        return False, False
           
def single_frame():
    stream = io.BytesIO()
    cfg.camera.capture(stream, 'jpeg', use_video_port=True)
    stream.seek(0)
    frame = stream.read()
    return frame

#c = cv2.VideoCapture(0)    
class Camera(object):
    thread = None  # background thread that reads frames from camera
    frame = None  # current frame is stored here by background thread
    last_access = 0  # time of last client access to the camera
    c = None

    def initialize(self):
        if Camera.thread is None:
            #self.c = cv2.VideoCapture(0)
            #print('camera started')
            # start background frame thread
            Camera.thread = threading.Thread(target=self._thread)
            Camera.thread.start()

            # wait until frames start to be available
            while self.frame is None:
                #print('aaa')
                time.sleep(0)

    def get_frame(self):
        #self.c = camera_handle
        Camera.last_access = time.time()
        self.initialize()
        return self.frame

    

    @classmethod
    def _thread(cls):
        

        while(True):
            _, cls.frame = cfg.camera_handle.read()

            #cls.frame = cv2.resize(cls.frame, (320,240))

            


        cls.thread = None
