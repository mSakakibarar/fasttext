from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

import fasttext as ft

class Category1(APIView):
    def get(self, request, text, format=None):
        classifier = ft.load_model("data/results/result.bin")
        return Response({"category1": classifier.predict(text)})

class Category2(APIView):
    def get(self, request, text, format=None):
        classifier = ft.load_model("data/results/result.bin")
        return Response({"category1": classifier.predict(text)})
