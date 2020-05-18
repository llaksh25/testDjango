
# outsource packages
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser, FileUploadParser, MultiPartParser, FormParser
# from rest_framework.permissions import IsAuthenticated
# custom folders
from imageFile.models import ImageModel
from imageFile.serializers import ImageSerializer


@api_view(['POST'])
@parser_classes([FormParser, MultiPartParser])
# @permission_classes([IsAuthenticated])
def post_image(request):
    post_serializer = ImageSerializer(data=request.data)
    if post_serializer.is_valid():
        post_serializer.save()
        return Response(post_serializer.data, status=status.HTTP_201_CREATED, content_type='application/json')
    else:
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_view(request):
    get_all = ImageModel.objects.all()
    get_serializer = ImageSerializer(get_all, many=True)
    return Response(get_serializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete(request):

    is_true = ImageModel.objects.filter(userName__exact=request.data.get("userName")).count()
    if is_true > 0:
        delete = ImageModel.objects.get(userName__exact=request.data.get("userName"))
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        delete.delete()
        return Response('Delete Successfully', status=status.HTTP_202_ACCEPTED)


