import cv2 
import pytesseract

'''
# Set the path to the Tesseract executable
# Uncomment and set the correct path for your system if necessary
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Windows example

# Load the image
image_path = "C:/Users/zuhair.aziz/Desktop/python/damageTracker_project/img/image3.png"
image = cv.imread(image_path, cv.IMREAD_REDUCED_COLOR_2)

# Convert to grayscale
# Convert to grayscale
if image is None:
    print("Image not loaded properly")
    #raise ValueError("Image not loaded properly")
else:
    print("Image succesfully loaded")
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

# Apply thresholding
_, binary_image = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)



# Display the binary image
cv.imshow('Binary Image', binary_image)
cv.waitKey(0)  # Wait for a key press to close the image window
cv.destroyAllWindows()

'''
'''
def init_control_gui():

    TRACKBAR_WINDOW = "Trackbars"

    cv.namedWindow(TRACKBAR_WINDOW, cv.WINDOW_NORMAL)
    cv.resizeWindow(TRACKBAR_WINDOW, 350, 700)

    # required callback. we'll be using getTrackbarPos() to do lookups
    # instead of using the callback.
    def nothing(position):
        pass

    # create trackbars for bracketing.
    # OpenCV scale for HSV is H: 0-179, S: 0-255, V: 0-255
    cv.createTrackbar('HMin', TRACKBAR_WINDOW, 0, 179, nothing)
    cv.createTrackbar('SMin', TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('VMin', TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('HMax', TRACKBAR_WINDOW, 0, 179, nothing)
    cv.createTrackbar('SMax', TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('VMax', TRACKBAR_WINDOW, 0, 255, nothing)
    # Set default value for Max HSV trackbars
    cv.setTrackbarPos('HMax', TRACKBAR_WINDOW, 179)
    cv.setTrackbarPos('SMax', TRACKBAR_WINDOW, 255)
    cv.setTrackbarPos('VMax', TRACKBAR_WINDOW, 255)

    # trackbars for increasing/decreasing saturation and value
    cv.createTrackbar('SAdd', TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('SSub', TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('VAdd', TRACKBAR_WINDOW, 0, 255, nothing)
    cv.createTrackbar('VSub', TRACKBAR_WINDOW, 0, 255, nothing)


#init_control_gui()

'''

