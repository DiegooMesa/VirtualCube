import cv2

def color_reader(h,s):

    color = "undefined"
    if h >= 0 and h <= 10 and s > 100 and s <= 255:
        color = "RED"
    elif h>10 and h<=25 and s > 100 and s <= 255:
        color = "ORANGE"
    elif h>25 and h<=40 and s > 100 and s <= 255:
        color = "YELLOW"
    elif h>35 and h<=75 and s > 100 and s <= 255:
        color = "GREEN"
    elif h>75 and h<130 and s > 100 and s <= 255:
        color = "BLUE"
    elif s < 100:
        color = "WHITE"
    else: 
        color = "UNDEFINED"
    
    return color

def color2rgb (color):
    if color == "RED":
        rgb = (0, 0, 255)
    elif color == "ORANGE":
        rgb = (0, 100, 255)
    elif color == "YELLOW":
        rgb = (0, 255, 255)
    elif color == "GREEN":
        rgb = (0, 210, 100)
    elif color == "BLUE":
        rgb = (219, 70, 29)
    elif color == "WHITE":
        rgb = (255, 255, 255)
    else:
        rgb = (0,0,0)
    
    return rgb

def face_color (center):
    h = center[0]
    s = center[1]
    color = color_reader(h,s)
    return color

def input(face_color):
    if face_color == "WHITE":
        None