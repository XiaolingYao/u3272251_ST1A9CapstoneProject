import pickle
import numpy as np
import pandas as pd
from scipy.special import inv_boxcox


# Set the Class PredictionModel as Superclass
class PredictionModel:
    def __init__(self, model):
        self.__model = model
        # Load the model from a file
        with open(self.__model, 'rb') as f:
            self.__model = pickle.load(f)
        print(f"Prediction Model loaded from {self.__model}")

    @property
    def model(self):
        return self.__model

    def predict(self, data):
        return self.__model.predict(data)


# Set the Class boxcoxY_XGBPredictor(The model we used in this assignment) as the Subclass of PredictionModel
# Because the original target variable price is right-skewed, we built the regression with normalised target varibale: boxcox(price) in stead.
# Therefore, u3272251XGB.kpl will give the prediction of boxcox(price), and we will need to convert it back to the price.
class boxcoxY_XGBPredictor(PredictionModel):
    __BestLambda = -0.06699
    def __init__(self, model):
        PredictionModel.__init__(self, model)
        self.__model = model

    def predict(self, data):
        return round(inv_boxcox(super().predict(data)[0], self.__BestLambda), 2)
