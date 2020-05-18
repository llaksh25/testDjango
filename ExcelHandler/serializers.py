from rest_framework import serializers
from import_export import resources
from ExcelHandler.models import TestExcel


class ExcelSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestExcel
        fields = fields = ('id', 'name', 'age', 'gender')
        # export_order = ('id', 'name', 'gender', 'age')
        # fields = '__all__'


class ExcelResources(resources.ModelResource):
    class Meta:
        model = TestExcel
        fields = ('id', 'name', 'age', 'gender')
        # export_order = ('id', 'name', 'gender', 'age')
        # fields = '__all__'