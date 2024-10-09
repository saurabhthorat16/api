
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Item
from .Serializer import ItemSerializer
# Create your views here.


@api_view(['GET','POST'])
def item_list(request):
    if request.method =="GET":
        items = Item.objects.all()
        serializer = ItemSerializer(items,many=True)
        return Response(serializer.data)

    elif request.method=="POST":
        serializer = ItemSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)













