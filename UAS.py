import cv2
import numpy as np


def image1() :
    def image() :  
        global img 
        img = cv2.imread("1.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE1",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL1",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority

    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        
        blur=cv2.medianBlur(mask,9,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and tri.ravel()[1] < 400 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  AND ALSO IF ITS Y IS LESS THAN 400
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[1] > 400 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  AND ALSO IF ITS Y IS GREATER THAN 400 
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,9,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and tri.ravel()[1] < 400 : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  AND ALSO IF ITS Y IS LESS THAN 400
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[1] > 400 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  AND ALSO IF ITS Y IS GREATER THAN 400
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image2() :
    def image() :  
        
        global img 
        img = cv2.imread("2.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
       
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE2",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL2",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority


    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        
        blur=cv2.medianBlur(mask,11,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and (tri.ravel()[0] < 358 or tri.ravel()[1] > 415) :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  AND ALSO IF ITS Y IS LESS THAN 400
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] > 358 and tri.ravel()[1] < 415 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  AND ALSO IF ITS Y IS GREATER THAN 400 
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,9,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and (tri.ravel()[0] < 364 or tri.ravel()[1] > 396)  : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  AND ALSO IF ITS Y IS LESS THAN 400
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] > 364 and tri.ravel()[1] < 396 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  AND ALSO IF ITS Y IS GREATER THAN 400
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image3() :
    def image() :  
        
        global img 
        img = cv2.imread("3.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE3",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL3",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority


    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        
        blur=cv2.medianBlur(mask,11,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and tri.ravel()[0] > 230 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] < 230:  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,9,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and tri.ravel()[0] > 230  : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] < 230 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image4() :
    def image() :  
        
        global img 
        img = cv2.imread("4.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE4",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL4",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority

    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        
        blur=cv2.medianBlur(mask,9,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and tri.ravel()[0] > 495 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] < 495 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,9,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and tri.ravel()[0] > 485  : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] < 485 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image5() :
    def image() :  
        
        global img 
        img = cv2.imread("5.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE5",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL5",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority
    
    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        
        blur=cv2.medianBlur(mask,9,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and tri.ravel()[1] < 475 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[1] > 475 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,9,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and tri.ravel()[1] < 475  : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[1] > 475 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image6() :
    def image() :  
        
        global img 
        img = cv2.imread("6.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE6",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL6",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority


    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        
        blur=cv2.medianBlur(mask,9,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and tri.ravel()[0] > 210 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] < 210 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,9,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and tri.ravel()[0] > 210 : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] < 210 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image7() :
    def image() :  
        
        global img 
        img = cv2.imread("7.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE7",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL7",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority
    
    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        
        blur=cv2.medianBlur(mask,9,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and tri.ravel()[0] < 174 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] > 174 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,9,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and tri.ravel()[0] < 174 : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] > 174 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image8() :
    def image() :  
        
        global img 
        img = cv2.imread("8.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE8",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL8",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority


    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        


        blur=cv2.medianBlur(mask,11,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and (tri.ravel()[0] < 370 or tri.ravel()[1] > 344 ) :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and (tri.ravel()[0] > 370 and tri.ravel()[1] < 344 ) :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,11,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and (tri.ravel()[0] < 350 or tri.ravel()[1] > 344 ) : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and tri.ravel()[0] > 350 and tri.ravel()[1] < 344 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image10() :
    def image() :  
        
        global img 
        img = cv2.imread("10.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO

        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE10",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL10",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority


    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        


        blur=cv2.medianBlur(mask,11,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and  tri.ravel()[1] < 460 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and  tri.ravel()[1] > 460 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,11,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and  tri.ravel()[1] < 460 : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and  tri.ravel()[1] > 460 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()
def image11() :
    def image() :  
        
        global img 
        img = cv2.imread("11.png")
        
        A= burnt_grass(img)
        B = grass(img)

        Crb,Crg=red_house(img)
        Cbb,Cbg=blue_house(img)

        Hb=Crb+Cbb
        Hg=Crg+Cbg
        houses = [Hb,Hg]   # TO GET A LIST WITH NUMBER OF HOUSES IN BURNT AND GREEN

        Pb= Crb*1  +  Cbb*2
        Pg= Crg*1  +  Cbg*2
        priority = [Pb,Pg]  # TO GET A LIST WITH PRIORITY 

        Pr= Pb/Pg  # TO GET THE RESCUE RATIO
        print(type(Pr))
        print(houses)  

        print(priority)
        
        print(Pr)


        merge= cv2.bitwise_or(A,B)  # GETTING THE IMAGE WITH DIFFERNRT COLOURS FOR DIFFERENT REGIONS
        # cv2.imshow("MERGE11",merge) 
        final=cv2.bitwise_or(merge,img)
        cv2.imshow("FINAL11",final)
        if cv2.waitKey(0)==ord("q") :
            exit()
        return priority

    def grass(img) :  # FOR CHANGING THE COLOUR OF NON BURNT REGION

        blur=cv2.medianBlur(img,9) # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        
        #TO GET THE LOWER AND UPPER RANGE OF GREEN
        l_green=np.array([0,50,0])          
        u_green=np.array([20,200,100])

        mask_green=cv2.inRange(blur,l_green,u_green)   # TO FIND ONLY GRASS REGION
        
        # CREATING A BLANK IMAGE OF A SPECIFIC COLOUR
        color_img=np.zeros((640,640,3),dtype=np.uint8)  # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[0,145,175]     # THIS GIVES THE COLOUR TO THE BLANK IMAGE

        grass_=cv2.bitwise_and(color_img,color_img,mask=mask_green)  #USING BITWISE AND OPERATION TO MERGE TWO IMAGES

    
        return grass_


    def burnt_grass(img) :  # TO COLOUR THE BURNT GRASS AREA

        blur=cv2.medianBlur(img,9)    # DID MEDIAN BLUR TO SMOTHEN TH EDGES AND TO REDUCE THE NOISE
        
        #TO GET THE LOWER AND UPPER RANGE OF BROWN
        l_brown=np.array([0,15,20])
        u_brown=np.array([30,52,100])

        mask_brown=cv2.inRange(blur,l_brown,u_brown)  # TO FIND ONLY BURNT REGION
        
        color_img=np.zeros((640,640,3),dtype=np.uint8)   # THIS CREATES A BLANK IMAGE OF THE GIVEN DIMENSIONS 
        color_img[:]=[150,150,1]  # THIS GIVES THE COLOUR TO THE BLANK IMAGE
        

        grass_burnt=cv2.bitwise_and(color_img,color_img,mask=mask_brown)    #USING BITWISE AND OPERATION TO MERGE TWO IMAGES


        return grass_burnt


    def red_house(img) :   # TO FIND THE NUMBER OF RED HOUSE 

        #CALCULATION OF RED HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF RED 
        lower_r=np.array([0,0,100])  
        upper_r=np.array([100,100,255])

        mask=cv2.inRange(img,lower_r,upper_r) #TO GET ONLY THE RED HOUSES
        


        blur=cv2.medianBlur(mask,11,0)  # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE RED TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO FIND THE TRIANGLES
            
            
            if len(tri) == 3 and  tri.ravel()[0] > 200 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and  tri.ravel()[0] < 200 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1   # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of red houses on burnt area")
        print(count_nonburnt,"Total no. of red houses on non burnt area")
        return count_burnt,count_nonburnt

    def blue_house(img) :# TO FIND THE NUMBER OF BLUE HOUSE 

        #CALCULATION OF BLUE HOUSES 
        
        #TO GET THE LOWER AND UPPER RANGE OF BLUE 
        lower_b=np.array([100,0,0])
        upper_b=np.array([255,120,120])

        mask=cv2.inRange(img,lower_b,upper_b)  #TO GET ONLY THE BLUE HOUSES

        blur=cv2.medianBlur(mask,11,0)   # TO REDUCE THE NOISE

        contours,_ = cv2.findContours(blur,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)  # TO FIND THE CONTOURS OF THE BLUE TRIANGLE
        
        count_burnt = 0
        count_nonburnt = 0
        for contour in contours : 

            tri = cv2.approxPolyDP(contour,0.05*cv2.arcLength(contour,True),True)  # TO GET THE COUNTERS OF A TRIANGLE
            
            
            if len(tri) == 3 and  tri.ravel()[0] > 200 : #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_burnt += 1     # TO COUNT THE NUMBER OF TRIANGLES IN BURNT AREA

            if len(tri) == 3 and  tri.ravel()[0] < 200 :  #TO EXECUTE ONLY IF THE LENGTH OF TRI ARRAY IS THREE / TRI.RAVEL IS USED SO THAT A ND ARRAY 
                                                        #CAN BE CONVERTED TO A 1D ARRAY  
                
                count_nonburnt += 1    # TO COUNT THE NUMBER OF TRIANGLES IN GRASS AREA

            
        print(count_burnt,"Total no. of blue houses on burnt area")
        print(count_nonburnt,"Total no. of blue houses on non burnt area")
        return count_burnt,count_nonburnt


    image()


def findcolour() :
    def pick_color(event,x,y,flags,param):   # TO FIND THE COLOUR OF THE REGION OF THE IMAGE  ON WHICH I CLICK
        if event == cv2.EVENT_LBUTTONDOWN :   # TO CHECK IF LEFT MOUSE BUTTON IS CLICKED
            bgr_color = img1[y,x]      # TO DISPLAY THE BGR VALUE AT X,Y
            print(f"BGR color at ({x},{y}):{bgr_color}")

    cv2.namedWindow("IMAGE")
    cv2.setMouseCallback("IMAGE",pick_color)   # TO ACCESS pick_color WHENEVER THE MOUSE IS CLICKED
    img1=cv2.imread("11.png")

    cv2.imshow("IMAGE",img)

    if cv2.waitKey(0)==ord("q") :
        exit()


#findcolour()
image1 =image1()
image2= image2()
image3=image3()
image4=image4()
image5=image5()
image6=image6()
image7=image7()
image8=image8()
image10=image10()
image11=image11()

list2 = [image1,image2,image3,image4,image5,image6,image7,image8,image10,image11]

list2.sort(reverse=True)
print(list2)

