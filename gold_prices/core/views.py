from rest_framework import generics, permissions
from .models import (
    MilliGoldModel,
    TalaseModel,
    TlynModel
)
from .serializer import (
    MilliGoldSerializers,
    TalaseSerializers,
    TlynSerializers
)


class MilliGoldList(generics.ListAPIView):
    queryset = MilliGoldModel.objects.all()
    serializer_class = MilliGoldSerializers
    permission_classes = [permissions.AllowAny]


class TalaseList(generics.ListAPIView):
    queryset = TalaseModel.objects.all()
    serializer_class = TalaseSerializers
    permission_classes = [permissions.AllowAny]


class TlynList(generics.ListAPIView):
    queryset = TlynModel.objects.all()
    serializer_class = TlynSerializers
    permission_classes = [permissions.AllowAny]


