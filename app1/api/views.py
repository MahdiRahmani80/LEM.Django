from app1.models import Music , User, Report
from app1.api.serializers import musicSerializer , userSerializer , reportSerializer
from rest_framework import generics

class create(generics.CreateAPIView):
    queryset = Music.objects.all()
    serializer_class = musicSerializer


class show(generics.ListAPIView):
    queryset = Music.objects.all()
    serializer_class = musicSerializer

class update(generics.RetrieveUpdateAPIView):
    queryset = Music.objects.all()
    serializer_class = musicSerializer
    lookup_field = 'id'

class user(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = userSerializer
    lookup_field = 'id'

class createUser(generics.CreateAPIView):
    queryset = User.username
    serializer_class = userSerializer

#  Change
class reportMusic(generics.CreateAPIView):
    queryset = Report.objects.all()
    serializer_class = reportSerializer
    lookup_field = 'id'
