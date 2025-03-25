import cv2
import numpy as np
import time

# Callback function for trackbars (do nothing)
def nothing(x):
    pass

# Main function to play the video for a specified duration
def play_video(video_path, duration):

    start_time = time.time()
    cap = cv2.VideoCapture(video_path) 

    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    # Create a window for the video and the trackbars
    cv2.namedWindow('Video')
    cv2.namedWindow('Trackbars')

    cv2.createTrackbar("L - H", "Trackbars", 0, 179, nothing)
    cv2.createTrackbar("L - S", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 0, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 179, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

    
    paused = False

    while cap.isOpened():
        if not paused:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame.")
                break

            frame = cv2.resize(frame, (640, 480))
            

            l_h = cv2.getTrackbarPos("L - H", "Trackbars")
            l_s = cv2.getTrackbarPos("L - S", "Trackbars")
            l_v = cv2.getTrackbarPos("L - V", "Trackbars")
            u_h = cv2.getTrackbarPos("U - H", "Trackbars")
            u_s = cv2.getTrackbarPos("U - S", "Trackbars")
            u_v = cv2.getTrackbarPos("U - V", "Trackbars")
            # Define the lower and upper HSV range
            lower_bound = np.array([l_h, l_s, l_v])
            upper_bound = np.array([u_h, u_s, u_v])

            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            mask = cv2.inRange(hsv, lower_bound, upper_bound)
            result = cv2.bitwise_and(frame, frame, mask=mask) 


            # Display the modified frame
            cv2.imshow('Video', result)
        
            if time.time() - start_time > duration:
                break

            # Wait for 30 milliseconds between frames
            key = cv2.waitKey(50) & 0xFF
            if key == ord('q') or cv2.getWindowProperty('Video', cv2.WND_PROP_VISIBLE) < 1:
                break
            elif key == ord('p'):
                paused = not paused

    cap.release()
    cv2.destroyAllWindows()

video_path = 'video/sample1.mp4'
duration = 30  # Play the video for 30 seconds
play_video(video_path, duration)
