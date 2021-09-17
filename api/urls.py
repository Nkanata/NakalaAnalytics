from django.conf.urls import url
from .views import ApiRoot, CountryList, ContinentList, DataList, DataDetail, CountryDetail, ContinentDetail

urlpatterns = [
    url(r'^countries/$', CountryList.as_view(), name=CountryList.name),
    url(r'^countries/(?P<pk>[0-9]+)$', CountryDetail.as_view(), name=CountryDetail.name),
    url(r'^continents/$', ContinentList.as_view(), name=ContinentList.name),
    url(r'^continents/(?P<pk>[0-9]+)$', ContinentDetail.as_view(), name=ContinentDetail.name),
    url(r'^data/$', DataList.as_view(), name=DataList.name),
    url(r'^data/(?P<pk>[0-9]+)$', DataDetail.as_view(), name=DataDetail.name),
    url(r'^$', ApiRoot.as_view(), name=ApiRoot.name)
]
