from rest_framework import serializers
from Home.models import getModel
from imageFile.serializers import TestSerializer


class homeSerializer(serializers.ModelSerializer):
    # test = TestSerializer()
    class Meta:
        model = getModel;
        # fields = '__all__';
        #fields = ['username', 'password', 'email_address', 'phone_number'];
        # fields = ('id','username', 'password', 'email_address', 'phone_number', 'test'); # table joins
        fields = ('id', 'username', 'password', 'email_address', 'phone_number')
