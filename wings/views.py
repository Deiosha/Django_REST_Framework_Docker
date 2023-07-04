from rest_framework import generics
from .serializers import WingSerializer
from .models import Wing
from .permissions import IsOwnerOrReadOnly


class WingList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Wing.objects.all()
    serializer_class = WingSerializer


class WingDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Wing.objects.all()
    serializer_class = WingSerializer
