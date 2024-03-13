from django.shortcuts import render
from django.http import *
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer


# Create your views here.
@api_view(("POST",))
def file_upload(request):
    data = None
    if request.method == "POST":
        data = request.FILES["file_upload"]
        reader = pd.read_excel(
            data,
            sheet_name=0,
            header=2,
        )
        print(reader.shape[0])
        # print(reader.loc[0])
        customers = []
        label_index = [0, 1, 4, 16]
        for i in range(0, reader.shape[0]):
            customer = {
                "ship_code": "",
                "contact_name": "",
                "order_type": "",
                "total_tons": "",
            }
            count = 0
            for i1 in label_index:
                if count == 0:
                    customer["ship_code"] = reader.iloc[i, i1]
                elif count == 1:
                    customer["contact_name"] = reader.iloc[i, i1]
                elif count == 2:
                    customer["order_type"] = reader.iloc[i, i1]
                elif count == 3:
                    customer["total_tons"] = reader.iloc[i, i1]
                count += 1
            customers.append(customer)
        print(customers)

    return Response(customers, status=status.HTTP_200_OK)
