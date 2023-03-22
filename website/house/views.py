from django.shortcuts import render
from .model import HousePricePredictor
from sklearn.impute import KNNImputer
import numpy as np


def my_form(request):
    predicted_price = None
    if request.method == 'POST':
       
        predictor = HousePricePredictor()
        input_features = {}
        for feature in predictor.features:
            # check if the feature was selected in the form
            if feature in request.POST.getlist('features'):
                input_features[feature] = request.POST[feature]
                
        
        # Find the missing values using KNN imputer
        imputer = KNNImputer(n_neighbors=38)
        all_features = np.array([float(input_features.get(feature, np.nan)) for feature in predictor.features])
        print("before imputation", all_features)
        imputed_features = imputer.fit_transform([all_features])[0]
        print("after imputation: ", imputed_features)
        
        # Update the input_features dictionary with the imputed values
        i = 0
        for feature in predictor.features:
            if feature not in input_features:

                input_features[feature] = imputed_features[i]
                print(f"imputed_features{[feature]}, {input_features[feature]}")
                i += 1
        
        # Make the prediction using the HousePricePredictor model
        predicted_price = predictor.predict(input_features)
        print("predicted_price: ", predicted_price)
        
    return render(request, 'house/my_form.html', {'predicted_price': predicted_price})

# input_features = {
            #     'MSSubClass': request.POST['MSSubClass'],
            #     'MSZoning': request.POST['MSZoning'],
            #     'LotFrontage': request.POST['LotFrontage'],
            #     'LotArea': request.POST['LotArea'],
            #     'Street': request.POST['Street'],
            #     'LotShape': request.POST['LotShape'],
            #     'LandContour': request.POST['LandContour'],
            #     'LotConfig': request.POST['LotConfig'],
            #     'LandSlope': request.POST['LandSlope'],
            #     'Neighborhood': request.POST['Neighborhood'],
            #     'Condition1': request.POST['Condition1'],
            #     'Condition2': request.POST['Condition2'],
            #     'BldgType': request.POST['BldgType'],
            #     'HouseStyle': request.POST['HouseStyle'],
            #     'OverallQual': request.POST['OverallQual'],
            #     'OverallCond': request.POST['OverallCond'],
            #     'YearBuilt': request.POST['YearBuilt'],
            #     'YearRemodAdd': request.POST['YearRemodAdd'],
            #     'RoofStyle': request.POST['RoofStyle'],
            #     'RoofMatl': request.POST['RoofMatl'],
            #     'Exterior1st': request.POST['Exterior1st'],
            #     'Exterior2nd': request.POST['Exterior2nd'],
            #     'MasVnrType': request.POST['MasVnrType'],
            #     'MasVnrArea': request.POST['MasVnrArea'],
            #     'ExterQual': request.POST['ExterQual'],
            #     'ExterCond': request.POST['ExterCond'],
            #     'Foundation': request.POST['Foundation'],
            #     'BsmtQual': request.POST['BsmtQual'],
            #     'BsmtCond': request.POST['BsmtCond'],
            #     'BsmtExposure': request.POST['BsmtExposure'],
            #     'BsmtFinType1': request.POST['BsmtFinType1'],
            #     'BsmtFinSF1': request.POST['BsmtFinSF1'],
            #     'BsmtFinType2': request.POST['BsmtFinType2'],
            #     'BsmtFinSF2': request.POST['BsmtFinSF2'],
            #     'BsmtUnfSF': request.POST['BsmtUnfSF'],
            #     'TotalBsmtSF': request.POST['TotalBsmtSF'],
            #     'Heating': request.POST['Heating'],
            #     'HeatingQC': request.POST['HeatingQC'],
            #     'CentralAir': request.POST['CentralAir'],
            #     'Electrical': request.POST['Electrical'],
            #     'FirstFlrSF': request.POST['FirstFlrSF'],
            #     'SecondFlrSF': request.POST['SecondFlrSF'],
            #     'LowQualFinSF': request.POST['LowQualFinSF'],
            #     'GrLivArea': request.POST['GrLivArea'],
            #     'BsmtFullBath': request.POST['BsmtFullBath'],
            #     'BsmtHalfBath': request.POST['BsmtHalfBath'],
            #     'FullBath': request.POST['FullBath'],
            #     'HalfBath': request.POST['HalfBath'],
            #     'BedroomAbvGr': request.POST['BedroomAbvGr'],
            #     'KitchenAbvGr': request.POST['KitchenAbvGr'],
            #     'KitchenQual': request.POST['KitchenQual'],
            #     'TotRmsAbvGrd': request.POST['TotRmsAbvGrd'],
            #     'Functional': request.POST['Functional'],
            #     'Fireplaces': request.POST['Fireplaces'],
            #     'GarageType': request.POST['GarageType'],
            #     'GarageYrBlt': request.POST['GarageYrBlt'],
            #     'GarageFinish': request.POST['GarageFinish'],
            #     'GarageCars': request.POST['GarageCars'],
            #     'GarageArea': request.POST['GarageArea'],
            #     'GarageQual': request.POST['GarageQual'],
            #     'GarageCond': request.POST['GarageCond'],
            #     'PavedDrive': request.POST['PavedDrive'],
            #     'WoodDeckSF': request.POST['WoodDeckSF'],
            #     'OpenPorchSF': request.POST['OpenPorchSF'],
            #     'EnclosedPorch': request.POST['EnclosedPorch'],
            #     'ThirdSsnPorch': request.POST['ThirdSsnPorch'],
            #     'ScreenPorch': request.POST['ScreenPorch'],
            #     'PoolArea': request.POST['PoolArea'],
            #     'MiscVal': request.POST['MiscVal'],
            #     'MoSold': request.POST['MoSold'],
            #     'YrSold': request.POST['YrSold'],
            #     'SaleType': request.POST['SaleType'],
            #     'SaleCondition': request.POST['SaleCondition'],
                
            #     # add more features here
            # }






