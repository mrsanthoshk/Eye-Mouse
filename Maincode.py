import cv2 #To image precessing
import mediapipe as mp  # To detect the eye mov
import pyautogui  #for the mouse connections.
cam = cv2.VideoCapture(0) #To cap the image
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)  #Link to mp as fashmesh  #we have total 478 LM in our face.
screen_w, screen_h = pyautogui.size()  #to get the screen size adn give to the pyautogui
while True:  #To run on everyframe..
    _, frame = cam.read()  #frame as a cam
    frame = cv2.flip(frame, 1)  # as in general we'll get the opp image -after this we'll get a normal pic.
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  #change the frame and into colour as -2
    output = face_mesh.process (rgb_frame) #shows the outputrun..
    landmark_points = output.multi_face_landmarks  # we can see the points of our face in the op - x ,y ,z
    frame_h, frame_w, _ = frame.shape  # we dont care for the dimension "_"  the shape as frame
    if(landmark_points): 
        landmarks = landmark_points[0].landmark  # from 0 as 1 to all the face 
        for id,  landmark in enumerate(landmarks[474:478]):  #for the eye this is the LM.  #enumerate-it wil give the ID and LM
            x = int(landmark.x * frame_w)  #to see the area we want or the area of our face../z no need as by the axs.
            y = int(landmark.y * frame_h)        #adding "int" to get a normal no. coz as in general well get a floating number
            cv2.circle(frame, (x,y), 3, (192, 192, 192))  #to draw the circle on the frame
            if id == 1:
                screen_x = int(landmark.x*screen_w)  #for scaling the screen to the cur to move.
                screen_y = int(landmark.y*screen_h)
                pyautogui.moveTo(screen_x, screen_y) #to move the cur to the points
        left = [landmarks[145],landmarks[159]] # fro the eye lashes.
        for landmark in left : #for the left eye just a variable
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x,y), 3, (0, 255, 255))
        if (left[0].y - left[1].y) < 0.004:  #for left we have 2 index so 0 and 1 as starting y - vertical #0.. for the output to solve.
            pyautogui.click()  # to make the cur to click - opeartion
            pyautogui.sleep(1) # and in normal if not click

    cv2.imshow('Eye Controlled Mouse', frame)  #To show some on the cam
    cv2.waitKey(1)   