from rest_framework import serializers
from .models import TalaseModel, TlynModel, MilliGoldModel



class MilliGoldSerializers(serializers.ModelSerializer):
        class Meta:
            model = MilliGoldModel
            fields = '__all__'



class TalaseSerializers(serializers.ModelSerializer):
        class Meta:
            model = TalaseModel
            fields = '__all__'


class TlynSerializers(serializers.ModelSerializer):
        class Meta:
            model = TlynModel
            fields = '__all__'

