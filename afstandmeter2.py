import cv2
import numpy as np

drawing = False # True if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix, iy = -1, -1

# mouse callback function
def draw_circle(event, x, y, flags, param):
    global ix, iy, drawing, mode, overlay, output, alpha
    overlay = img.copy()
    output = img.copy()
    alpha = 0.5

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                pass
                #cv2.rectangle(overlay, (ix, iy), (x, y), (0, 255, 0), 0)
                #cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, img)
                #cv2.imshow('image', img)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(overlay, (ix, iy), (x, y), (0, 255, 0), 0)
            cv2.addWeighted(overlay, alpha, output, 1 - alpha, 0, img)
            print("Wat is de echte hoogte van het object, de sensorhoogte en de focal length?")
            s=3.42
            f=4.42
            h=input("Echte hoogte object:")
            h = int(h)

            print(abs(y-iy), img.shape[0], h, s, f)
            print()
            dis=(f*h*img.shape[0])/(abs(y-iy)*s)
            print(dis)

img = cv2.imread("img1.jpg", 1)
#make cv2 windows, set mouse callback
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while(1):
    cv2.imshow('image', img)
    # This is where we get the keyboard input
    # Then check if it's "m" (if so, toggle the drawing mode)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    if k == ord('d'):
        img = cv2.imread("img1.jpg", 1)
    elif k == 27:
        break

cv2.destroyAllWindows()