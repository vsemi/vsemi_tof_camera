import numpy as np
import cv2
import time
import sys

from TauLidarCommon.frame import FrameType
from TauLidarCamera.camera import Camera

def setup(port = None):
    camera = None
    
    if not port:
        ports = Camera.scan()                      ## Scan for available Tau Camera devices

        if len(ports) > 0:
            port = ports[0]
    
    Camera.setRange(0, 4500)                   ## points in the distance range to be colored

    print("\nOpenning ToF camera at serial port ", port, ' ...')
    camera = Camera.open(port)
    camera.setModulationChannel(0)             ## autoChannelEnabled: 0, channel: 0
    camera.setIntegrationTime3d(0, 1000)       ## set integration time 0: 1000
    camera.setMinimalAmplitude(0, 10)          ## set minimal amplitude 0: 80
    camera.setIntegrationTimeGrayscale(10000)  ## set integration time grayscale: 8000, needed when requiring FrameType.DISTANCE_GRAYSCALE

    cameraInfo = camera.info()

    print("\nToF camera opened successfully:")
    print("    model:      %s" % cameraInfo.model)
    print("    firmware:   %s" % cameraInfo.firmware)
    print("    uid:        %s" % cameraInfo.uid)
    print("    resolution: %s" % cameraInfo.resolution)
    print("    port:       %s" % cameraInfo.port)

    print("\nPress Esc key over GUI or Ctrl-c in terminal to shutdown ...")

    return camera

def variance_of_laplacian(image):
    # compute the Laplacian of the image and then return the focus
    # measure, which is simply the variance of the Laplacian
    return cv2.Laplacian(image, cv2.CV_64F).var()

def run(camera):
    start_t = time.time()
    frame_count = 0
    cameraInfo = camera.info()
    uid = cameraInfo.uid

    try:
        count = 0
        maxfocus = 0
        while True:
            '''
            To require FrameType.DISTANCE_GRAYSCALE frame
            '''
            frame = camera.readFrame(FrameType.DISTANCE_GRAYSCALE)
            # frame = camera.readFrame(FrameType.DISTANCE_AMPLITUDE)

            if frame == None: 
                sleep(0.1)
                continue

            count += 1

            mat = np.frombuffer(frame.data_grayscale, dtype=np.uint16, count=-1, offset=0).reshape(frame.height, frame.width)
            mat = mat.astype(np.uint8)

            # mat = np.frombuffer(frame.data_amplitude, dtype=np.float32, count=-1, offset=0).reshape(frame.height, frame.width)
            # mat = mat.astype(np.uint8)
    
            upscale = 4
            img =  cv2.resize(mat, (160*upscale, 60*upscale))
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)

            focus = variance_of_laplacian(mat)
            if focus > maxfocus:
            	maxfocus = focus

            #print('%d / %d'%(focus, maxfocus))
            font = cv2.FONT_HERSHEY_SIMPLEX 
            fontScale = 0.8
            
            color = (0, 0, 255)
            q = focus / maxfocus
            #print("{:.2f}".format(q))
            if q > 0.9:
            	color = (0, 255, 0)

            img = cv2.putText(img, 'ID:', (5, 30), font, fontScale, (255, 0, 0), 1, cv2.LINE_AA, False)
            img = cv2.putText(img, '%s'%cameraInfo.uid, (60, 30), font, fontScale, (0, 255, 0), 1, cv2.LINE_AA, False)
            img = cv2.putText(img, 'Focus (Current / Max):', (5, 60), font, fontScale, (255, 0, 0), 1, cv2.LINE_AA, False)
            img = cv2.putText(img, '%d / %d'%(focus, maxfocus), (320, 60), font, fontScale, color, 1, cv2.LINE_AA, False)

            cv2.imshow('Sensor ID: %s'%cameraInfo.uid, img)

            if cv2.waitKey(1) == 27: break

    except KeyboardInterrupt:    
        print('\nShutting down ...')
        cv2.destroyAllWindows()
        sleep(0.1)
        camera.close()
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

def cleanup(camera):
    print('\nShutting down ...')
    cv2.destroyAllWindows()
    camera.close()

if __name__ == "__main__":

    port = None
    if len(sys.argv) > 1:
        port = sys.argv[1]
    
    camera = setup(port)

    if camera:
        try:
            run(camera)
        except Exception as e:
            print(e)

        cleanup(camera)
