import cv2
import numpy as np

img = cv2.imread("UAS WORKS\Screenshot 2024-10-02 091911.png")




def grass() :  #for changing the colour of non burnt region

    blur=cv2.medianBlur(img,3)   #did median blur to smothen th edges
    l_green=np.array([0,50,0])     
    u_green=np.array([100,255,100])

    mask_green=cv2.inRange(blur,l_green,u_green)   #to find only non burnt region
    
    

    
    color_img=np.zeros((438,437,3),dtype=np.uint8)  # creating a image of a specific colour
    color_img[:]=[0,145,175]

    grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #using bitwise operation to merge two images

    # cv2.imshow("ONLY GRASS",grass_)

    
    return grass_


def burnt_grass() :  # to colour the burnt grass area

    blur=cv2.medianBlur(img,5)
    l_brown=np.array([0,15,30])
    u_brown=np.array([10,40,70])

    mask_brown=cv2.inRange(blur,l_brown,u_brown)
    


    color_img=np.zeros((438,437,3),dtype=np.uint8)
    color_img[:]=[150,150,1]

    grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)

    # cv2.imshow("ONLY BURNT GRASS",grass_burnt)
   
   
    return grass_burnt

  

A = burnt_grass()
B = grass()


merge= cv2.bitwise_or(A,B)  # getting the image with differnrt colours for different regions
cv2.imshow("FINAL",merge) 
print(type(merge)) 

img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
_,thresh=cv2.threshold(img_gray,74,80,cv2.THRESH_BINARY)



cv2.imshow("zsb",thresh)


# edge=cv2.Canny(img_gray,75,78)
contour,h = cv2.findContours(img_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contour,-1,(0,255,0),6)



def pick_color(event,x,y,flags,param):   # to find the colour of the region of the image
    if event == cv2.EVENT_LBUTTONDOWN :
        bgr_color = img_gray[y,x]
        print(f"BGR color at ({x},{y}):{bgr_color}")

cv2.namedWindow("IMAGE")
cv2.setMouseCallback("IMAGE",pick_color)

cv2.imshow("IMAGE",img_gray)
cv2.imshow("new",img)

if cv2.waitKey(0)==ord("q") :
    exit()
