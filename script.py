import numpy as np
import cv2 as cv


def capture_video():
    """Capture video from webcam using opencv"""
    # create VideoCapture obj with device index (camera #) as input
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        print("cannot open camera")
        exit()

    while True:
        # capture camera input frame-by-frame
        ret, frame = cap.read()

        # ret is True if frame captured correctly
        if not ret:
            print('cant recieve frame')
            break

        # operate on the captured frame - convert to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # show modified frame
        cv.imshow('frame', frame)
        cv.imshow('gray', gray)
        if cv.waitKey(1) == ord('q'):
            break

    # release after everything is done !important
    cap.release()
    cv.destroyAllWindows()


def capture_video2file():
    """Capture video from webcam using opencv and
    write video to file"""

    # capture video output
    cap = cv.VideoCapture(0)

    # define codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print('Frame cannot be received. Exiting...')
            break
        # flip the received frame
        frame = cv.flip(frame, 0)
        # write the new frame to file
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break

    # release everything once job is done
    cap.release()
    out.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    capture_video()
