from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Continent, Country, Data
from .serializers import ContinentSerializer, CountrySerializer, DataSerializer
from rest_framework import filters
from django_filters import AllValuesFilter, DateTimeFilter, NumberFilter
from rest_framework import permissions


# Create your views here.

class ContinentList(generics.ListAPIView):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    name = 'continent-list'
    filter_fields = ('continent',)
    search_fields = (
        '^continent',
    )
    ordering_fields = (
        'continent',
    )
    permission_classes = (permissions.IsAuthenticated,)


class ContinentDetail(generics.RetrieveAPIView):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
    name = 'continent-detail'
    permission_classes = (permissions.IsAuthenticated,)


class CountryList(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    name = 'country-list'
    filter_fields = ('country',)
    search_fields = (
        '^country',
        '^iso_code',
    )
    ordering_fields = (
        'country',
    )
    permission_classes = (permissions.IsAuthenticated,)


class CountryDetail(generics.RetrieveAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    name = 'country-detail'
    permission_classes = (permissions.IsAuthenticated,)


class DataList(generics.ListAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    name = 'data-list'
    filter_fields = ('country',)
    search_fields = (
        '^country',
    )
    ordering_fields = (
        'country',
        'date',
    )
    permission_classes = (permissions.IsAuthenticated,)


class DataDetail(generics.RetrieveAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    name = 'data-detail'
    permission_classes = (permissions.IsAuthenticated,)


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    @staticmethod
    def get(request, *args, **kwargs):
        return Response({
            'continents': reverse(ContinentList.name, request=request),
            'countries': reverse(CountryList.name, request=request),
            'data': reverse(DataList.name, request=request)
        })
    permission_classes = (permissions.IsAuthenticated,)
