
# download excel package
from django.http import HttpResponse

# rest framework package
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser, JSONParser
from rest_framework.decorators import parser_classes

# custom folders
from ExcelHandler.models import TestExcel
from ExcelHandler.serializers import ExcelResources, ExcelSerializer
from singleMethods.constructExcel import construct_excel

# openpyxl
from openpyxl.writer.excel import save_virtual_workbook
from openpyxl import load_workbook

#import excel
import tablib
import pandas as pd


@api_view(['GET'])
def open_pyxl(request):
    data = TestExcel.objects.all()
    get_serializer = ExcelSerializer(data, many=True);
    result = construct_excel(get_serializer)

    res = HttpResponse(content=save_virtual_workbook(result), content_type='application/ms-excel')
    res['Content-Disposition'] = 'attachment; filename="table.xls"'
    return res


@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
def post_excel(request):
    # wb_obj = load_workbook(testing)
    testing = request.data.get('test')
    if testing.name.endswith('.xls') or testing.name.endswith('.xlsx'):
        # 'Sheet' fetch particular worksheet
        worksheet_data = pd.read_excel(testing, 'Sheet', index_col=None)
        worksheet_data.to_csv('your_csv.csv', encoding='utf-8')
    else:
        worksheet_data = pd.read_csv(testing)

    resource = ExcelResources()
    data_set = tablib.Dataset()
    data_set.load(worksheet_data)
    result = resource.import_data(data_set, dry_run=True)    # Test the data import
    if not result.has_errors():
        resource.import_data(data_set, dry_run=False)   # Actually import now
        return Response({'success': 'True', 'message': 'data saved successfully'}, status=status.HTTP_201_CREATED,
                        content_type='application/json')
    else:
        return Response(resource.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
# @parser_classes([FormParser, MultiPartParser])
def import_export_package(request):
    data_set = ExcelResources().export()
    # print(data_set.csv)
    res = HttpResponse(data_set.csv, content_type='text/csv', status=status.HTTP_201_CREATED)
    res['Content-Disposition'] = 'attachment; filename="persons.csv"'
    return res

    # Json format download
    """
    response = HttpResponse(dataset.json, content_type='application/json')
    response['Content-Disposition'] = 'attachment; filename="persons.json"'
    """

    # xls & xlsx format download
    """
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="persons.xls"'
    """






