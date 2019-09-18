from django.shortcuts import render
from django.views import View
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class TestView(APIView):

    def post(self, request):
        print('query:', request.query_params)
        print('data:', request.data)
        return Response({'result': 1})

    def get(self, request):
        print('query: ', request.query_params)
        return Response({'result': 1})
