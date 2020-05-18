from rest_framework import serializers
from imageFile.models import ImageModel, Test


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageModel;
        fields = '__all__';
        # fields = ['username', 'password', 'email_address', 'phone_number'];


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Test;
        fields = '__all__';