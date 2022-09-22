from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response
from .models import WorkInfor
from .serializer import WorkInforSerialize
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView, ListAPIView


# Create your views here.

class IsReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True


class WorkinforViewSet(viewsets.ModelViewSet):
    queryset = WorkInfor.objects.all().order_by('id')
    serializer_class = WorkInforSerialize
    permissions_classes = [permissions.IsAuthenticated]

    # def get_queryset(self):
    #     queryset = WorkInfor.objects.all().order_by('id')
    #     return queryset

class ListPagination(PageNumberPagination):
    page_size = 9
    page_size_query_param = 'page_size'

    def get_paginated_response(self, data):
        return Response({
            'numItems': self.page.paginator.count,
            'totalPages': self.page.paginator.num_pages,
            'pageSize': self.page_size,
            'currentPage': self.page.number,
            'data': data,
        })


class GetListWorkInfo(ListCreateAPIView):
    pagination_class = ListPagination
    serializer_class = WorkInforSerialize
    permission_classes = [AllowAny]

    def get_queryset(self):
        print(12397123917293)
        return WorkInfor.objects.all().order_by('id')

    def create(self, request, *args, **kwargs):
        data = self.request.data
        WorkName_text = data.get('WorkName_text')
        Company_text = data.get('Company_text')
        level = data.get('level')
        Description_text = data.get('Description_text')
        LongTime = data.get('LongTime')
        phone_number = data.get('phone_number')
        photo = data.get('photo')
        money = data.get('money')

        workinfor = WorkInfor.objects.create(
            WorkName_text=WorkName_text,
            Company_text=Company_text,
            level=level,
            Description_text=Description_text,
            LongTime=LongTime,
            phone_number=phone_number,
            photo=photo,
            money=money,
        )

        return Response({
            'ok': True,
            'data': WorkInforSerialize(workinfor).data
        })





# def work_info_detail(request):
#
#
#     if request.method == 'GET':
#         try:
#             work_info = WorkInfor.objects.all().order_by('id')
#         except WorkInfor.DoesNotExit:
#             return Response(status=status.HTTP_404_NOT_FOUND)
#         serializer = WorkInforSerialize(work_info, many=True, context={'request': request})
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         print(1)
#
#         # Cách 1 by anh Hiệp
#
#         data = request.data
#         WorkName_text = data.get('WorkName_text')
#         Company_text = data.get('Company_text')
#         level = data.get('level')
#         Description_text = data.get('Description_text')
#         LongTime = data.get('LongTime')
#         phone_number = data.get('phone_number')
#         photo = data.get('photo')
#         money = data.get('money')
#         print(photo, 34235435436465465)
#         workinfor = WorkInfor.objects.create(
#             WorkName_text=WorkName_text,
#             Company_text=Company_text,
#             level=level,
#             Description_text=Description_text,
#             LongTime=LongTime,
#             phone_number=phone_number,
#             photo=photo,
#             money=money,
#         )
#         return Response({
#             'ok': True,
#             'data': WorkInforSerialize(workinfor).data
#         })
#     # Cách 2 by doc of rest-Django
#     # serializer = WorkInforSerialize(data=request.data)
#     # if serializer.is_valid():
#     #     serializer.save()
#     #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#     # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         work_info = WorkInfor.objects.order_by('LongTime')
#         return Response(status=status.HTTP_204_NO_CONTENT)




