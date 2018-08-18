# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Companies
from .serializers import CompaniesSerializer


@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_company(request, pk):
    try:
        company = Companies.objects.get(pk=pk)
    except Companies.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single company
    if request.method == 'GET':
        serializer = CompaniesSerializer(company)
        return Response(serializer.data)
    # delete a single company
    elif request.method == 'DELETE':
        company.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single company
    elif request.method == 'PUT':
        serializer = CompaniesSerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_companies(request):
    # get all companies
    if request.method == 'GET':
        return Response({})
    # insert a new record for a company
    elif request.method == 'POST':
        return Response({})
