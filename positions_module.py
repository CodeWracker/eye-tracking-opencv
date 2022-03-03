import cv2
import numpy as np
import pandas as pd
from definitions import *
class PositionsModule():
    def __init__(self):
        self._data = []
    
    def add_positions(self,eyeData):
        self._data.append(eyeData)

    def get_past_n_positions(self,n):
        left_eye = []
        right_eye = []
        for i in range(len(self._data)):
            eyeData = self._data[len(self._data)-(1+i)]
            if(i>n):
                break
            left_eye.append([eyeData._left_iris["x"],eyeData._left_iris['y']])
            right_eye.append([eyeData._right_iris["x"],eyeData._right_iris['y']])
        return left_eye,right_eye
    def save_data(self,path):
        df = pd.DataFrame()
        left_iris_x = []
        left_iris_y = []

        right_iris_x = []
        right_iris_y = []


        left_pupil_x = []
        left_pupil_y = []

        right_pupil_x = []
        right_pupil_y = []

        frame = []
        for i in range(len(self._data)):
            left_iris_x.append(self._data[i]._left_iris['x'] if self._data[i]._left_iris else "")
            left_iris_y.append(self._data[i]._left_iris['y'] if self._data[i]._left_iris else "")

            right_iris_x.append(self._data[i]._right_iris['x'] if self._data[i]._right_iris else "")
            right_iris_y.append(self._data[i]._right_iris['y'] if self._data[i]._right_iris else "")


            left_pupil_x.append(self._data[i]._left_pupil['x'] if self._data[i]._left_pupil else "")
            left_pupil_y.append(self._data[i]._left_pupil['y'] if self._data[i]._left_pupil else "")

            right_pupil_x.append(self._data[i]._right_pupil['y'] if self._data[i]._right_pupil else "")
            right_pupil_y.append(self._data[i]._right_pupil['y'] if self._data[i]._right_pupil else "")

            frame.append(self._data[i]._frame if self._data[i]._frame != None else "")
        

        df["frame"] = frame 


        df["left_iris_x"] = left_iris_x 
        df["left_iris_y"] = left_iris_y 

        df["right_iris_x"] = right_iris_x 
        df["right_iris_y"] = right_iris_y 


        df["left_pupil_x"] = left_pupil_x 
        df["left_pupil_y"] = left_pupil_y 

        df["right_pupil_x"] = right_pupil_x 
        df["right_pupil_y"] = right_pupil_y 

        df.to_csv(path)


class EyeDataModule():
    def __init__(self,frame):
        self._left_iris = None
        self._right_iris = None
        self._left_pupil = None
        self._right_pupil = None
        self._frame = frame

    def add_left_iris(self, left_iris):
        (x,y),r = left_iris
        
        self._left_iris = {
                    "x": x,
                    "y": y,
                    "r": r
                }
    def add_right_iris(self, right_iris):
        (x,y),r = right_iris
        self._right_iris = {
                    "x": x,
                    "y": y,
                    "r": r
                }
    def add_left_pupil(self, left_pupil):
        (x,y),r = left_pupil
        
        self._left_pupil = {
                    "x": x,
                    "y": y,
                    "r": r
                }
    def add_right_pupil(self, right_pupil):
        (x,y),r = right_pupil
        
        self._right_pupil = {
                    "x": x,
                    "y": y,
                    "r": r
                }

        