from django.shortcuts import render
from django.http import JsonResponse
from ubajax.models import UbntModelTest, DataUbntall
import ubajax.busilog as bus
from plotly.offline import plot
from plotly.graph_objs import Scatter
import os


def restartreq(request):
    os.system('systemctl restart selenoneprog.service')
    return render(request, 'ubajax/vazar_light.html')


def schedulel(request, periodurl):
    """Формирует данные для отображения на странице статистики локального IP адреса"""
    # periodurl представляет из себя строку '10.1.11.206_16'
    # отделяем IP адрес от периода

    url = periodurl.split('_')[0]
    period = int(periodurl.split('_')[1])

    # ----------------Это просто чтобы не забыть----------------------------------------
    # получаем самую последнюю запись
    #    timedata = DataUbntall.objects.filter(ipubnttwo=url).order_by('timewrite')[0]
    # ----------------------------------------------------------------------------------
    
    data96 = DataUbntall.objects.filter(ipubnttwo=url)
    # Определяем колличество записей за 96 часов
    dl96 = len(data96)
    # Получаем за 16 часов
    dl16 = round(dl96 / 8)
    data = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0:72]

    x_data = []
    y_data = []
    for x in range(0, 72):
        y_data.append(data[x].udprml0*(-1))
        x_data.append(data[x].timewrite)
    plot_div = plot([Scatter(x=x_data, y=y_data,
                    mode='lines', name='test',
                    opacity=0.8, marker_color='green')],
                    output_type='div')
    return render(request, 'ubajax/schedulel.html', context={'plot_div': plot_div})

def scheduler(request, periodurl):
    """Формирует данные для отображения на странице статистики удалённого IP адреса"""
    # periodurl представляет из себя строку '10.1.11.206_16'
    # отделяем IP адрес от периода
    url = periodurl.split('_')[0]
    period = int(periodurl.split('_')[1])

    data96 = DataUbntall.objects.filter(ipubnttworem=url)
    dl96 = len(data96)
    # Получаем за 16 часов
    dl16 = round(dl96 / 8)
    data = DataUbntall.objects.filter(ipubnttworem=url).order_by('-timewrite')[0:72]

    x_data = []
    y_data = []
    for x in range(0,72):
        y_data.append(data[x].udprmr0 * (-1))
        x_data.append(data[x].timewrite)
    plot_div = plot([Scatter(x=x_data, y=y_data,
                    mode='lines', name='test',
                    opacity=0.8, marker_color='green')],
                    output_type='div')
    return render(request, 'ubajax/scheduler.html', context={'plot_div': plot_div})



def ubntstart(request):
    return render(request, 'ubajax/index.html')


def ubntsmart(request):
    return render(request, 'ubajax/indexsmart.html')

def startapi(request):
    """Формирует данные для AJAX на главной странице реализованного на VUE.JS"""
    data = bus.data_ready(bus.iplist())
    return JsonResponse(data)


def apinav(request):
    """Формирует данные для AJAX на навигационной панели реализованного на VUE.JS"""
    data = bus.data_ready_nav(bus.iplist())
    return JsonResponse(data)

def apiphone(request, ipubntone):
    """Формирует данные для AJAX для передачи на смартфон"""
    data = bus.data_ready_phone(ipubntone)
    return JsonResponse(data)

def apiphonelist(request):
    """Формирует список IP адресов для AJAX для передачи на смартфон"""
    data = bus.iplistphone()
    return JsonResponse(data)

def detail(request, ipubntone):
    """Формирует страницу 'Подробно' для локального IP"""
    return render(request, 'ubajax/detail.html', context={'data_detail': bus.detail_all(ipubntone)})


def detailrem(request, ipubntone):
    """Формирует страницу 'Подробно' для удалённого IP"""
    return render(request, 'ubajax/detailrem.html', context={'data_detail': bus.detail_all(ipubntone)})


def statlocal(request, periodurl):
    """Формирует страницу 'Статистика РРС' для локального IP"""
    # periodurl представляет из себя строку '10.1.11.206_24'
    # отделяем IP адрес от периода
    dd = bus.statl(periodurl)
    return render(request, 'ubajax/statloc.html', context=dd)


def statremote(request, periodurl):
    """Формирует страницу 'Статистика РРС' для удалённого IP"""
    # periodurl представляет из себя строку '10.1.11.206_24'
    # отделяем IP адрес от периода
    dd = bus.statr(periodurl)
    return render(request, 'ubajax/statrem.html', context=dd)


def vazar_light(request):
    """Формирует страницу разработчика 'Контроллера РРС'"""
    return render(request, 'ubajax/vazar_light.html')


def mistakes_l(request, ipl):
    """Формирует страницу статистики ошибок доступа к РРС для локального IP"""
    data = DataUbntall.objects.filter(ipubnttwo=ipl).order_by('-timewrite')
    dataname = UbntModelTest.objects.get(ipubntone__iexact=ipl)
    return render(request, 'ubajax/mistakel.html', context={'data': data, 'dataname': dataname})


def mistakes_r(request, ipr):
    """Формирует страницу статистики ошибок доступа к РРС для удалённого IP"""
    data = DataUbntall.objects.filter(ipubnttworem=ipr).order_by('-timewrite')
    dataname = UbntModelTest.objects.get(ipubntremote__iexact=ipr)
    return render(request, 'ubajax/mistaker.html', context={'data': data, 'dataname': dataname})
