from django.shortcuts import render
from .serializers import ClientSerializer
from rest_framework import viewsets
from .models import Client


# Create your views here.
class ClientViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self):
        return self.queryset.filter(created_by=self.request.user)