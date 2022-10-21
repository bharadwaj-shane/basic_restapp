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
    result = multi(100,100,10)
    return Response(result, status=status.HTTP_201_CREATED)

@api_view(['POST'])
def calculate(request, format=None):
    """API to process long running application"""
    # data = json.load(request.data)
    # print("\val1:", data['k1'])
    # print("\val2:", data['k2'])
    result = multi(request.data['row1'],request.data['row2'],request.data['col'])
    return Response(result, status=status.HTTP_201_CREATED)


def multi(row1, row2, col):
    res_dict = {"Result": []}

    random_data1 = np.random.rand(row1, col)
    random_data2 = np.random.rand(row2, col)

    df1 = pd.DataFrame(random_data1)
    df2 = pd.DataFrame(random_data2)

    result = df1.mul(df2)
    df_mean = result.mean()
    lst = df_mean.tolist()
    res_dict["Result"] = lst
    # sleep(20)
    return res_dict