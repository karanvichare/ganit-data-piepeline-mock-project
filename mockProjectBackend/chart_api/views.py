# python dependencies
import logging
import traceback
import json

# Django rest framework related dependencies
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core import serializers

# Project related dependencies
from .models import CurrencyTypes
from .models import CurrencyData
from .serializers import CurrenyDataRequestSerializer


# Create your views here.


class CurrencyController(APIView):
    log = logging.getLogger(__name__)

    def get(self, request):
        """
        get function is used to give json response

        @param request: request parameter helps in accessing json request

        @returns- returns json response 

        """
        python_res = {
            'status_code': 400
        }
        try:
            currency_types = list(CurrencyTypes.objects.all(
            ).values_list('currency_type', flat=True))
            python_res = {
                'currency_types': currency_types,
                'status_code': 200
            }

        except Exception as error:
            self.log.error(error)
            python_res = {
                'error': error,
                'status_code': 201
            }
        finally:
            return Response(python_res, status=status.HTTP_200_OK, headers=None)


class ChartController(APIView):
    log = logging.getLogger(__name__)

    def post(self, request):
        """
        post function is used to give json response

        @param request: request parameter helps in accessing json request

        @returns- returns json response 

        """

        python_res = {
            'status_code': 400
        }

        try:
            serializer = CurrenyDataRequestSerializer(
                data=request.data)
            print(request.data,"request.data")
            if serializer.is_valid():
                print(serializer.data['currency'])
                currency_types = CurrencyData.objects.all().filter(currency_type=serializer.data['currency']).values('date', 'value')
                print(list(currency_types))
                # data = serializers.serialize('json', currency_types)
                # print(data,"data")
                python_res = {
                    'currency_types': list(currency_types),
                    'status_code': 200
                }
                
            else:
                self.log.error("not found currency")
                python_res = {
                    'error': 'currency not found',
                    'status_code': 201
                }

        except Exception as error:
            self.log.error(error)
            python_res = {
                'error': error,
                'status_code': 201
            }
        finally:
            return Response(python_res, status=status.HTTP_200_OK, headers=None)
