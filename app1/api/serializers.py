from app1.models import Music , User
from rest_framework.serializers import ModelSerializer

class musicSerializer(ModelSerializer):
    class Meta:
        model  = Music
        fields = '__all__'

class userSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
