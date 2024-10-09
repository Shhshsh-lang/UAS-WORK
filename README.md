# UAS-WORK
uas task for round 2

2 OCTOBER 2024
I downloaded Ubuntu  but was getting some issues in opencv 
So I switched to windows 

3 OCTOBER 2024
Today I started doing my task
I have done the basics of opencv by the video  (  https://youtu.be/oXlwWbU8l2o?si=aV4NdlhGLxLru7Li ) (I have not completed the full video) today 
Then I started my task

thought of converting bgr to hsv then to do masking since it is more efficient but in hsv image everything was of same colour so i rejected it
then i did masking using bgr and i also used median blur for more accuracy
but I was not able to get the colour range 
So I asked gunmay bhaiya then he gave me the solution 
Till now I have just made the grassy area with different colour

4 OCTOBER 2024
today i made the burnt area with different colour in a different image
and also merged both the images to get the burnt and non burnt area with different colour on the same image
then i tried finding the number of triangles 
for this i refered to youtube and found different methods (i would be going to use method in which cv2.polydp() method is used )
for this i needed contours but in gray image i was not getting the blue tringlei 
i tried but am not able to solve it

5 OCTOBER 2024
Previously I was converting the original image to gray but this time I converted merged image to gray then I got all the triangles 
Then I found its contours and then the number of triangles using cv2.approxpolydp()
(Not asked to do)

Then I my mergerd image the triangles were black but I needed them in colour 
So first I converted the image using bitwise not so that I get the triangle area as white instead of black then I used bitwise or with the original and the merged image 


6th October 
Today I found the number of red and blue triangles on each region 
For this I first used the red colour mask to get the red triangles on both region and also for blue triangles 
But getting blue and red triangles of only a specific region was bit tough so I used the coordinates of the contours of the triangles to do it the i did the rest of calculation 
Till now  I have completed the work on a single image

7th October
today i applied the same code on all the test images since i used the coordinates to differnciate between the grassy and burnt area so i had to do this 

