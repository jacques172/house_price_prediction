import pickle
import numpy as np

class HousePricePredictor:
    def __init__(self):
        with open('model.pkl', 'rb') as f:
            self.model = pickle.load(f)
        # Define the list of feature names expected by the model
        self.features = [  'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea', 'Street',    'LotShape', 'LandContour',
                          'LotConfig', 'LandSlope', 'Neighborhood',    'Condition1', 'Condition2',
                          'BldgType', 'HouseStyle', 'OverallQual',    'OverallCond', 'YearBuilt', 'YearRemodAdd', 
                          'RoofStyle', 'RoofMatl', 'Exterior1st', 'Exterior2nd', 'MasVnrType', 'MasVnrArea', 'ExterQual',   
                          'ExterCond', 'Foundation', 'BsmtQual', 'BsmtCond', 'BsmtExposure',    'BsmtFinType1', 'BsmtFinSF1',
                            'BsmtFinType2', 'BsmtFinSF2', 'BsmtUnfSF',    'TotalBsmtSF', 'Heating', 'HeatingQC', 'CentralAir', 
                            'Electrical',    'FirstFlrSF','SecondFlrSF', 'LowQualFinSF', 'GrLivArea', 'BsmtFullBath',   
                              'BsmtHalfBath', 'FullBath', 'HalfBath', 'BedroomAbvGr', 'KitchenAbvGr',    'KitchenQual', 
                              'TotRmsAbvGrd', 'Functional', 'Fireplaces', 'GarageType',    'GarageYrBlt', 'GarageFinish', 'GarageCars',
                            'GarageArea', 'GarageQual',    'GarageCond', 'PavedDrive', 'WoodDeckSF', 'OpenPorchSF', 'EnclosedPorch', 
                                  'ThirdSsnPorch', 'ScreenPorch','PoolArea', 'MiscVal', 'MoSold', 'YrSold',    'SaleType', 'SaleCondition']


    def predict(self, features):
        # features is a dictionary with the input features for the prediction
        feature_vector = np.array([float(features[feature]) for feature in self.features])
        price = self.model.predict(feature_vector.reshape(1, -1))[0]
        return price
