from asyncore import read
from rest_framework import serializers
from ccfApp.models import fileSystem

class fileSystemSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    created_at = serializers.DateTimeField(read_only=True)
    size = serializers.IntegerField()
    
    class Meta:
        model = fileSystem
        fields="__all__"
        
    