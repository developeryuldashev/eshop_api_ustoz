from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.status import HTTP_201_CREATED,HTTP_204_NO_CONTENT,HTTP_200_OK

from utils.paginator import StandardResultsSetPagination
from .paginations import ProductPagination
from product.models import Product, Category
from product.serializers import ProductSerializer, CategorySerializer


class ProductViewset(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandardResultsSetPagination

    def list(self, request, *args, **kwargs):
        category = request.GET.get('category',None)
        queryset = self.get_queryset()
        if category:
            queryset = queryset.filter(category=category)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

# 335077373
# 977850172
class CategoryViewset(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def list(self, request, store_pk=None, locker_pk=None):
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        category=Category.objects.create(
            name=request.data.get('name',None),
            description=request.data.get('description',None),
        )
        return Response(data={'status':'created'},status=HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        category = Category.objects.get(pk=kwargs.get('pk'))
        category.name=request.data.get('name',None)
        category.description=request.data.get('description',None)
        category.save()

        return Response(status=HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        category=Category.objects.get(pk=kwargs.get('pk',None))
        category.delete()
        return Response(data={'status':'deleted'},status=HTTP_204_NO_CONTENT)



