import cv2
import numpy as np
import time
import RPi.GPIO as GPIO

#======================== Constants ========================#
# GPIO Pins
Motor1A = 16
Motor1B = 20
Motor1E = 21

Motor2A = 13
Motor2B = 19
Motor2E = 26

#======================== Hardware Control Functions ========================#
def forward():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)

    print("[Motor Action] Forward")
    return

def reverse():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
 
    print("[Motor Action] Reverse")
    return

def stop():
    GPIO.output(Motor1E,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.LOW)
 
    print("[Motor Action] Stopping")
    return

def left():
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.HIGH)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.HIGH)
    GPIO.output(Motor2B,GPIO.HIGH)
    GPIO.output(Motor2E,GPIO.HIGH)
 
    print("[Motor Action] Left")
    return

def right():
    GPIO.output(Motor1A,GPIO.LOW)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    
    GPIO.output(Motor2A,GPIO.LOW)
    GPIO.output(Motor2B,GPIO.LOW)
    GPIO.output(Motor2E,GPIO.HIGH)
 
    print("[Motor Action] Right")
    return

#======================== Visual Functions ========================#
def drawText(frame, text):
    cv2.putText(frame, text, (460,475), cv2.FONT_HERSHEY_PLAIN, 1.5, (0,255,0), 2, cv2.LINE_AA)
    return

# Function to determine whether the current input frame contains a sufficent
# number of red pixels.
def checkRed(frame, hsvFrame):
    lwRed = np.array([0,157,69])
    upRed = np.array([9, 255, 255])

    redMask = cv2.inRange(hsvFrame, lwRed, upRed)
    redRes = cv2.bitwise_and(frame, frame, mask = redMask)

    if cv2.countNonZero(redMask) > 200:
        return True
    
    return False


#======================== GPIO Pin Setup ========================#

GPIO.setmode(GPIO.BCM)
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)
GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)

#======================== Main ========================#
cap = cv2.VideoCapture(0)

# Main loop to determine whether or not to move forward.
while True:
    _, frame = cap.read()
    hsvFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) # convert to HSV

    # Visual Detection
    if checkRed(frame, hsvFrame) == True:
        print("[OpenCV] Colour Red Detected")
        print("[Motor] Stop")
        stop()
        drawText(frame, "Red Detected")
    else:
        forward()

    cv2.imshow("Frame", frame)
    time.sleep(2) # Delay to keep outputs constant for 2 seconds.
    GPIO.output(Motor1E,GPIO.LOW)
    
    # Exit Mechanism (ESC)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Clean-up
GPIO.cleanup()
cv2.destroyAllWindows()
cap.release
exit()
