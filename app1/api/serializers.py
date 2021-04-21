from app1.models import Music , User ,Report
from rest_framework.serializers import ModelSerializer

class musicSerializer(ModelSerializer):
    class Meta:
        model  = Music
        fields = '__all__'

class userSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

#  Change
class reportSerializer (ModelSerializer):
    class Meta:
        model = Report
        fields = '__all__'
