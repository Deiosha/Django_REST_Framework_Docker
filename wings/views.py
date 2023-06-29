from rest_framework import generics
from .serializers import WingSerializer
from .models import Wing


class WingList(generics.ListCreateAPIView):
    queryset = Wing.objects.all()
    serializer_class = WingSerializer


class WingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Wing.objects.all()
    serializer_class = WingSerializer
