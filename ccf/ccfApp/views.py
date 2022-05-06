from django.shortcuts import render
from rest_framework import generics
from django.views.generic import TemplateView,ListView
from ccfApp.serializers import fileSystemSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from ccfApp.models import fileSystem
from django.db.models import Q
from rest_framework import status

class HomePageView(TemplateView):
    template_name='home.html'
        
class search(ListView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name='search_result.html'
    serializer_class = fileSystemSerializer
    
    def get_queryset(self):
        query = self.request.GET.get('search_input')
        object_list = fileSystem.objects.filter(
            Q(title__icontains=query)
        )
        return object_list
        
    
