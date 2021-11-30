from django.urls import path

from ubajax.views import ubntstart, startapi, detail, \
    detailrem, apinav, statlocal, statremote, vazar_light, \
    mistakes_l, mistakes_r, apiphone, apiphonelist, ubntsmart, schedulel, scheduler, restartreq

urlpatterns = [
    path('', ubntstart, name='rrl_list_url'),
    path('api/', startapi, name='startapi_url'),
    path('apin/', apinav, name='startapin_url'),
    path('apiph/<str:ipubntone>/', apiphone, name='apiph_url'),
    path('apiphl/', apiphonelist, name='apiphl_url'),
    path('ip/<str:ipubntone>/', detail, name='rrs_detail_url'),
    path('ipr/<str:ipubntone>/', detailrem, name='rrs_detailrem_url'),
    path('mistakel/<str:ipl>/', mistakes_l, name='rrs_mistakel_url'),
    path('mistaker/<str:ipr>/', mistakes_r, name='rrs_mistaker_url'),
    path('smart', ubntsmart, name='rrl_list_smart_url'),
    path('statl/<str:periodurl>/', statlocal, name='rrs_statloc_url'),
    path('statr/<str:periodurl>/', statremote, name='rrs_statrem_url'),
    path('vazar/', vazar_light, name='vazar_light_url'),
    path('schedulel/<str:periodurl>/', schedulel, name='schedulel_url'),
    path('scheduler/<str:periodurl>/', scheduler, name='scheduler_url'),
    path('restartreq/', restartreq, name='restartreq_url'),
]

