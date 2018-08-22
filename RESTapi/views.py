# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import django_filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from .models import Companies
from .models import Basin
from .models import Facility
from .models import FixedEquipment
from .models import TmlInfo
from .models import Measurements
from .models import Users
from .serializers import CompaniesSerializer
from .serializers import BasinSerializer
from .serializers import FacilitySerializer
from .serializers import FixedEquipmentSerializer
from .serializers import TMLinfoSerializer
from .serializers import MeasurementsSerializer
from .serializers import UsersSerializer

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
        companies = Companies.objects.all()
        serializer = CompaniesSerializer(companies, many=True)
        return Response(serializer.data)
    # insert a new record for a company
    elif request.method == 'POST':
        return Response({})

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_basin(request, pk):
    try:
        basin = Basin.objects.get(pk=pk)
    except Basin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single company
    if request.method == 'GET':
        serializer = BasinSerializer(basin)
        return Response(serializer.data)
    # delete a single company
    elif request.method == 'DELETE':
        basin.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single company
    elif request.method == 'PUT':
        serializer = BasinSerializer(basin, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_basins(request):
    # get all companies
    if request.method == 'GET':
        basins = Basin.objects.all()
        serializer = BasinSerializer(basins, many=True)
        return Response(serializer.data)
    # insert a new record for a company
    elif request.method == 'POST':
        return Response({})

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_facility(request, pk):
    try:
        facility = Facility.objects.get(pk=pk)
    except Facility.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single company
    if request.method == 'GET':
        serializer = FacilitySerializer(facility)
        return Response(serializer.data)
    # delete a single company
    elif request.method == 'DELETE':
        facility.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single company
    elif request.method == 'PUT':
        serializer = FacilitySerializer(facility, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_facilities(request):
    # get all companies
    if request.method == 'GET':
        facilities = Facility.objects.all()
        serializer = FacilitySerializer(facilities, many=True)
        return Response(serializer.data)
    # insert a new record for a company
    elif request.method == 'POST':
        return Response({})

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_fixed_eqp(request, pk):
    try:
        fixed_eqp = FixedEquipment.objects.get(pk=pk)
    except FixedEquipment.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single company
    if request.method == 'GET':
        serializer = FixedEquipmentSerializer(fixed_eqp)
        return Response(serializer.data)
    # delete a single company
    elif request.method == 'DELETE':
        fixed_eqp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single company
    elif request.method == 'PUT':
        serializer = FixedEquipmentSerializer(fixed_eqp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_fixed_eqps(request):
    # get all companies
    if request.method == 'GET':
        fixed_eqps = FixedEquipment.objects.all()
        serializer = FixedEquipmentSerializer(fixed_eqps, many=True)
        return Response(serializer.data)
    # insert a new record for a company
    elif request.method == 'POST':
        return Response({})

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_tml(request, pk):
    try:
        tml = TmlInfo.objects.get(pk=pk)
    except TmlInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single company
    if request.method == 'GET':
        serializer = TMLinfoSerializer(tml)
        return Response(serializer.data)
    # delete a single company
    elif request.method == 'DELETE':
        tml.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single company
    elif request.method == 'PUT':
        serializer = TMLinfoSerializer(tml, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_tmls(request):
    # get all companies
    if request.method == 'GET':
        tmls = TmlInfo.objects.all()
        serializer = TMLinfoSerializer(tmls, many=True)
        return Response(serializer.data)
    # insert a new record for a company
    elif request.method == 'POST':
        return Response({})

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_measurement(request, pk):
    try:
        measurement = Measurements.objects.get(pk=pk)
    except Measurements.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single company
    if request.method == 'GET':
        serializer = MeasurementsSerializer(measurement)
        return Response(serializer.data)
    # delete a single company
    elif request.method == 'DELETE':
        measurement.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single company
    elif request.method == 'PUT':
        serializer = MeasurementsSerializer(measurement, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_measurements(request):
    # get all companies
    if request.method == 'GET':
        measurements = Measurements.objects.all()
        tml = request.GET.get('tml', None)
        if tml:
            measurements = measurements.filter(tml=tml)
        serializer = MeasurementsSerializer(measurements, many=True)
        return Response(serializer.data)
    # insert a new record for a company
    elif request.method == 'POST':
        return Response({})

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_user(request, pk):
    try:
        user = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single company
    if request.method == 'GET':
        serializer = UsersSerializer(user)
        return Response(serializer.data)
    # delete a single company
    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single company
    elif request.method == 'PUT':
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_users(request):
    # get all companies
    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)
    # insert a new record for a company
    elif request.method == 'POST':
        return Response({})
