from time import sleep
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
import pandas as pd
import numpy as np

# Create your views here.
@api_view(['GET'])
def calcnormal(request, format=None):
    """API to process long running application"""
    result = multi(10000, 10000, 10000, 10000)
    if result["Result"] != None :
        return Response(result, status=status.HTTP_201_CREATED)
    else :
        return Response(result, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def calculate(request, format=None):
    """API to process long running application"""
    result = multi(request.data['row1'],request.data['col1'],request.data['row2'],request.data['col2'])
    return Response(result, status=status.HTTP_201_CREATED)


def multi(row1, col1, row2, col2):
    if col1 != row2 :
        return {"Result": None}
    
    res_val = {}

    random_data1 = np.random.rand(row1, col1)
    random_data2 = np.random.rand(row2, col2)

    df1 = pd.DataFrame(random_data1)
    df2 = pd.DataFrame(random_data2)

    result = df1.dot(df2)
    df_mean = result.mean()
    df_std = result.std()
    lst_mean = df_mean.tolist()
    lst_std = df_std.tolist()
    res_val["Mean"] = lst_mean
    res_val["Std. Dev"] = lst_std
    # sleep(20)
    tot_res = {"Result":res_val}
    
    return tot_res
