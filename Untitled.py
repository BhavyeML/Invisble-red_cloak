#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system("pip install -r './requirements.txt'")
import cv2
import numpy as np


# In[ ]:


def bg_video():
    
    pic_file='image_capture.jpg'
    cap = cv2.VideoCapture(0)
    while cap.isOpened():
        ret, back = cap.read()
        if ret == True:
            cv2.imshow("image", back)
            if cv2.waitKey(5) == ord('c'):
                cv2.imwrite(pic_file, back)
                break
    return cap,pic_file


# In[ ]:


def invisible_cloak():
    
    cap = cv2.VideoCapture(0)

    back = cv2.imread('./image_capture.jpg')

    while cap.isOpened():
        ret, frame = cap.read()

        if ret:
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            
            #Choose color range based on your cloth color and make sure cloak's cloth and background's cloth are of same color
            l_red = np.array([0, 100, 100])
            u_red = np.array([10, 255, 255])

            mask = cv2.inRange(hsv, l_red, u_red)
            mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations = 2)
            mask = cv2.dilate(mask, np.ones((3, 3), np.uint8), iterations = 1)
        

            allred = cv2.bitwise_and(back, back, mask=mask)

            mask = cv2.bitwise_not(mask)

            notred = cv2.bitwise_and(frame, frame, mask=mask)


            cv2.imshow("cloak", allred+notred)

            if cv2.waitKey(5) == ord('c'):
                break

    cap.release()
    cv2.destroyAllWindows()


# In[ ]:


cap,pic_file=bg_video()
cap.release()
cv2.destroyAllWindows()


# In[ ]:



invisible_cloak()

