from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response


class Category1(APIView):
    def get(self, request, format=None):
        return Response({"category1": "カテゴリーを返す"})

class Category2(APIView):
    def get(self, request, format=None):
        return Response({"category2": "カテゴリーを返す"})
