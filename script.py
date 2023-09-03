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
        cv.imshow('gray_frame', gray)
        if cv.waitKey(1) == ord('q'):   # press 'q' on the frame shown to quit capture
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
    fourcc = cv.VideoWriter_fourcc(*'mp4v')
    fourcc_2 = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
    out2 = cv.VideoWriter('bw_output.avi', fourcc_2, 20, (640, 480), False)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print('Frame cannot be received. Exiting...')
            break
        # flip the received frame
        flip_frame = cv.flip(frame, 0)
        bw_frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # write the new frame to file
        out.write(frame)
        out2.write(bw_frame)
        cv.imshow('bw_frame', bw_frame)
        cv.imshow('frame', frame)
        # print(f'Frame Width x Height: {cap.get(cv.CAP_PROP_FRAME_WIDTH)} x {cap.get(cv.CAP_PROP_FRAME_HEIGHT)} ')
        # print(f'Backend: {cap.get(cv.CAP_PROP_BACKEND)}')
        if cv.waitKey(1) == ord('q'):
            break

    # release everything once job is done
    cap.release()
    out.release()
    out2.release()
    cv.destroyAllWindows()


def play_video_from_file():
    """Play video from file saved on disk"""

    # pass video file name instead of camera index
    cap = cv.VideoCapture('output.avi')

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print('Cannot receive frame. Exiting...')
            break

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        cv.imshow('frame', gray)
        if cv.waitKey(25) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


if __name__ == '__main__':
    # capture_video()           # capture and show video on screen

    capture_video2file()      # capture, show and save video to file

    # play_video_from_file()      # play video from file
