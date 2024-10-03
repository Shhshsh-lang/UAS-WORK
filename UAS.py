import cv2
import numpy as np

img = cv2.imread("UAS WORKS\Screenshot 2024-10-02 091911.png")


# img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def grass() :

    blur=cv2.medianBlur(img,3)
    l_green=np.array([0,50,0])
    u_green=np.array([100,255,100])

    mask_green=cv2.inRange(blur,l_green,u_green)
    
    

    # contour,h = cv2.findContours(mask_green,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    # cv2.drawContours(img,contour,0,(0,255,0),6)
    color_img=np.zeros((438,437,3),dtype=np.uint8)
    color_img[:]=[0,145,175]

    grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)


    cv2.imshow("IMAGE",grass_)
    if cv2.waitKey(0)==ord("r") :
        exit()

  
   

grass()

def pick_color(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN :
        bgr_color = img[y,x]
        print(f"BGR color at ({x},{y}):{bgr_color}")

cv2.namedWindow("IMAG")
cv2.setMouseCallback("IMAG",pick_color)

cv2.imshow("IMAG",img)
# cv2.imshow("new",img_gray)

if cv2.waitKey(0)==ord("q") :
    exit()
