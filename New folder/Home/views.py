from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# outsource packages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# custom folders
from Home.models import getModel
from imageFile.models import Test
from Home.serializers import homeSerializer


@api_view(['POST'])
def post_view(request):
    post_serializer = homeSerializer(data=request.data)
    if post_serializer.is_valid():
        post_serializer.save()
        return Response(post_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # return Response("Insert Successfully", status=status.HTTP_201_CREATED)  ---> ADD CUSTOM MESSAGE
    # return render(request)  --> DEFAULT RENDER DATA


@api_view(['GET'])
def get_view(request):
    get_all = getModel.objects.all()
    get_serializer = homeSerializer(get_all, many=True)
    return Response(get_serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_one(request, param):

    is_true = getModel.objects.filter(username=param).count()

    if is_true > 0:
        get_alone = getModel.objects.get(username=param)
        get_alone_serializer = homeSerializer(get_alone)
        return Response(get_alone_serializer.data, status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT', 'DELETE'])
def put_delete(request):

    is_true = getModel.objects.filter(username=request.data.get("username")).count()

    if is_true > 0:
        put_and_delete = getModel.objects.get(username=request.data.get("username"))
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        put_serializer = homeSerializer(instance=put_and_delete, data=request.data)
        if put_serializer.is_valid():
            put_serializer.save()
            return Response('Update Successfully', status=status.HTTP_201_CREATED)
        else:
            return Response(put_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        put_and_delete.delete()
        return Response('Delete Successfully', status=status.HTTP_202_ACCEPTED)


@api_view(['GET'])
def join(request):
    # test = getModel.objects.filter(username='test1').values_list('connKey', 'pk')
    test1 = getModel.objects.filter(username='test1')
    #test = getModel.objects.select_related('test').all();
    print (test1.query);
    test_joins = homeSerializer(test1, many=True)
    return Response(test_joins.data, status=status.HTTP_200_OK)
    """
    get_joins = getModel.objects.all()
    get_serializer = homeSerializer(get_all, many=True)
    return Response(get_serializer.data, status=status.HTTP_200_OK)
    """

"""
@api_view(['PUT', 'DELETE'])
def put_delete(request):
    try:
        #put_and_delete = getModel.objects.get(pk=1)
        put_and_delete = getModel.objects.get(username__exact=request.data.get("username"))
    except put_and_delete.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        put_serializer = homeSerializer(instance=put_and_delete, data=request.data)
        if put_serializer.is_valid():
            put_serializer.save()
            return Response(put_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(put_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        put_and_delete.delete()
        return Response('Delete Successfully', status=status.HTTP_202_ACCEPTED)
"""
