from datetime import datetime, timedelta
from ubajax.models import UbntModelTest, DataUbntall, Listipubnt, AutoRestart
import os


def iplist():
    """Формирует список IP адресов"""
    urls = UbntModelTest.objects.all()
    ip_all_ub = []
    for url in urls:
        if url.statonoff == 1:  # Если сигнал равен 1 - мониторинг разрешён
            # Добавляем IP адрес в список IP адресов учавствующих в мониторинге
            ip_all_ub.append(url)
        else:
            continue
    return ip_all_ub

def iplistphone():
    """Формирует список IP адресов для передачи в смартфон"""
    urls = UbntModelTest.objects.all()
    ip_all_ubphone = {}
    for url in urls:
        dname = UbntModelTest.objects.get(ipubntone=url)
        ip_all_ubphone[str(url)] = {'nameubntline': dname.nameubntline,
                                    'nameubnt': dname.nameubnt,
                                    'nameubntremote': dname.nameubntremote,
                                    'ipubntremote': dname.ipubntremote,
                                    }

    return ip_all_ubphone


def data_ready(urls):
    """Формирует пакет данных для отображения на главной странице"""
#    ppid = AutoRestart.objects.get(id=1)
#    sid = ppid.firstid
#    sch = ppid.schetchik
#    fsid = DataUbntall.objects.order_by('-timewtite')[0].id
#    if sch == 0:
#        sid = fsid
#        sch = 1
#        ppid.save()
#    elif sch == 10 and fsid == sid:
#        os.system('systemctl restart selenoneprog.service')
#        sch = 0
#        sid = 0
#        ppid.save()
#    else:
#        sch = sch + 1
#        ppid.save()
    data = {}
    for url in urls:
        try:
            dparam = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0]
            dname = UbntModelTest.objects.get(ipubntone=url)

            # получаю первую запись среди отфильтрованых по url прибавляю 96 часов (4 суток) и если
            # удовлетворяет условию удаляю запись
            dparam_del = DataUbntall.objects.filter(ipubnttwo=url).order_by('timewrite')[0]
            time_del = dparam_del.timewrite
            tt = time_del + timedelta(hours=96)
            tn = datetime.now()
            if tt <= tn:
                dparam_del.delete()

            if tn.hour == 7 and tn.minute == 0:
                listurls = ' '.join(iplist())
                lurl = Listipubnt.objects.get()
                lurl.current_list_ip = listurls
                lurl.save()

            if tn.hour == 18 and tn.minute == 0:
                lurl = Listipubnt.objects.get().current_list_ip
                listurl = lurl.split(' ')
                result = list(set(listurl) - set(iplist()))
                if result != []:
                    for ip in result:
                        os.remove(f'ip{ip}.txt')
                        ipubnt = DataUbntall.objects.filter(ipubnttwo=ip)
                        ipubnt.delete()

            if dname.statonoff == False:
                continue
            if dparam.udprml0 <= dname.prm_level or dparam.udprml0 == 0:
                flagsosl0 = 'ПРОБЛЕМА'
                prml0 = f'<span style="color:red"><strong>{dparam.udprml0}</strong></span>'
            else:
                flagsosl0 = 'НОРМА'
                prml0 = f'<span style="color:green"><strong>{dparam.udprml0}</strong></span>'

            if dparam.udprml1 <= dname.prm_level or dparam.udprml1 == 0:
                flagsosl1 = 'ПРОБЛЕМА'
                prml1 = f'<span style="color:red"><strong>{dparam.udprml1}</strong></span>'
            else:
                flagsosl1 = 'НОРМА'
                prml1 = f'<span style="color:green"><strong>{dparam.udprml1}</strong></span>'

            if dparam.udprmr0 <= dname.prm_level or dparam.udprmr0 == 0:
                flagsosr0 = 'ПРОБЛЕМА'
                prmr0 = f'<span style="color:red"><strong>{dparam.udprmr0}</strong></span>'
            else:
                flagsosr0 = 'НОРМА'
                prmr0 = f'<span style="color:green"><strong>{dparam.udprmr0}</strong></span>'

            if dparam.udprmr1 <= dname.prm_level or dparam.udprmr1 == 0:
                flagsosr1 = 'ПРОБЛЕМА'
                prmr1 = f'<span style="color:red"><strong>{dparam.udprmr1}</strong></span>'
            else:
                flagsosr1 = 'НОРМА'
                prmr1 = f'<span style="color:green"><strong>{dparam.udprmr1}</strong></span>'

            if flagsosl0 == 'ПРОБЛЕМА' or flagsosl1 == 'ПРОБЛЕМА':
                flagsos_rrsl = 'ПРОБЛЕМА'
                flagcolor_rrsl = '"badge badge-danger ml-5 mr-5"'
            else:
                flagsos_rrsl = 'НОРМА'
                flagcolor_rrsl = '"badge badge-success ml-5 mr-5"'

            if flagsosr0 == 'ПРОБЛЕМА' or flagsosr1 == 'ПРОБЛЕМА':
                flagsos_rrsr = 'ПРОБЛЕМА'
                flagcolor_rrsr = '"badge badge-danger ml-5 mr-5"'
            else:
                flagsos_rrsr = 'НОРМА'
                flagcolor_rrsr = '"badge badge-success ml-5 mr-5"'

            if flagsos_rrsl == 'ПРОБЛЕМА' or flagsos_rrsr == 'ПРОБЛЕМА':
                flagsos_rrl = 'ПРОБЛЕМА'
                flagcolor_rrl = '"badge badge-danger ml-5 mr-5"'
            else:
                flagsos_rrl = 'НОРМА'
                flagcolor_rrl = '"badge badge-success ml-5 mr-5"'

# Объекты класса datetime делаем строкой
            dtt = dparam.timewrite.strftime("%H:%M:%S")
            dtd = dparam.timewrite.strftime("%d.%m.%Y")

            data[str(url)] = {'udprml0': dparam.udprml0,
                              'udprml1': dparam.udprml1,
                              'udprmr0': dparam.udprmr0,
                              'udprmr1': dparam.udprmr1,
#                              'sl0': dparam.sl0,
#                              'sl01': f'width: {dparam.sl0}%;',
#                              'sl1': dparam.sl1,
#                              'sl11': f'width: {dparam.sl1}%;',
#                              'sr0': dparam.sr0,
#                              'sr01': f'width: {dparam.sr0}%;',
#                              'sr1': dparam.sr1,
#                              'sr11': f'width: {dparam.sr1}%;',
                              'udspeedl': dparam.udspeedl,
                              'udspeedr': dparam.udspeedr,
#                              'udnagrl': dparam.udnagrl,
#                              'udnagrr': dparam.udnagrr,
#                              'udnagrl_mk': dparam.udnagrl_mk,
#                              'udnagrr_mk': dparam.udnagrr_mk,
                              'ipubnttwo': dparam.ipubnttwo,
                              'ipubnttworem': dparam.ipubnttworem,
                              'nameubntline': dname.nameubntline,
                              'nameubnt': dname.nameubnt,
                              'nameubntremote': dname.nameubntremote,
                              'numberubntline': dname.numberubntline,
                              'flagsos_rrsl': flagsos_rrsl,
                              'flagcolor_rrsl': flagcolor_rrsl,
                              'flagsos_rrsr': flagsos_rrsr,
                              'flagcolor_rrsr': flagcolor_rrsr,
                              'flagsos_rrl': flagsos_rrl,
                              'flagcolor_rrl': flagcolor_rrl,
                              'lip': f'ip/{dparam.ipubnttwo}',
                              'rip': f'ipr/{dparam.ipubnttwo}',
                              'lipstatl': f'statl/{dparam.ipubnttwo}_16',
                              'ripstatr': f'statr/{dparam.ipubnttworem}_16',
                              'liphisl': f'schedulel/{dparam.ipubnttwo}_16',
                              'riphisr': f'scheduler/{dparam.ipubnttworem}_16',
                              'misl': f'mistakel/{dparam.ipubnttwo}',
                              'misr': f'mistaker/{dparam.ipubnttworem}',
                              'prml0': prml0,
                              'prml1': prml1,
                              'prmr0': prmr0,
                              'prmr1': prmr1,
                              'timewritet': dtt,
                              'timewrited': dtd,
                              'lipcros': f'http://{dparam.ipubnttwo}',
                              'ripcros': f'http://{dparam.ipubnttworem}',
                              }
        except Exception:
            continue
    return data


def data_ready_nav(urls):
    """Формирует пакет данных для отображения на навигационной панели"""
#    global name_rrl_danger
    dataflagl = []
    dataflagr = []
    for url in urls:
        try:
            dparam = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0]
            dname = UbntModelTest.objects.get(ipubntone=url)
            if dname.statonoff == False:
                continue
            if dparam.udprml0 <= dname.prm_level or dparam.udprml1 <= dname.prm_level or dparam.udprml0 == 0 or dparam.udprml1 == 0:
                flagsosln = 'ПРОБЛЕМА'
            else:
                flagsosln = 'НОРМА'

            if dparam.udprmr0 <= dname.prm_level or dparam.udprmr1 <= dname.prm_level or dparam.udprmr0 == 0 or dparam.udprmr1 == 0:
                flagsosrn = 'ПРОБЛЕМА'
            else:
                flagsosrn = 'НОРМА'

            dataflagl.append(flagsosln)
            dataflagr.append(flagsosrn)

            if flagsosln == 'ПРОБЛЕМА' or flagsosrn == 'ПРОБЛЕМА':
                name_rrl_danger = f'{dname.nameubntline}  '
        except Exception:
            continue

    if dataflagl.count('ПРОБЛЕМА') > 0 or dataflagr.count('ПРОБЛЕМА') > 0:
        flag_rrls = {'flagsos_rrls': 'ПРОБЛЕМА',
                     'flagcolor_rrls': '"badge badge-danger ml-5 mr-5"',
                     'name_rrl_danger': name_rrl_danger}
    else:
        flag_rrls = {'flagsos_rrls': 'НОРМА',
                     'flagcolor_rrls': '"badge badge-success ml-5 mr-5"'}

    return flag_rrls

def data_ready_phone(url):
    """Формирование данных для передачи в смартфон"""
    dparam = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0]
    dname = UbntModelTest.objects.get(ipubntone=url)
    data = {}
# Объекты класса datetime делаем строкой
    dtt = dparam.timewrite.strftime("%H:%M:%S")
    dtd = dparam.timewrite.strftime("%d.%m.%Y")

    data[str(url)] = {'udprml0': dparam.udprml0,
                      'udprml1': dparam.udprml1,
                      'udprmr0': dparam.udprmr0,
                      'udprmr1': dparam.udprmr1,
#                      'sl0': dparam.sl0,
#                      'sl01': f'width: {dparam.sl0}%;',
#                      'sl1': dparam.sl1,
#                      'sl11': f'width: {dparam.sl1}%;',
#                      'sr0': dparam.sr0,
#                      'sr01': f'width: {dparam.sr0}%;',
#                      'sr1': dparam.sr1,
#                      'sr11': f'width: {dparam.sr1}%;',
                      'udspeedl': dparam.udspeedl,
                      'udspeedr': dparam.udspeedr,
#                      'udnagrl': dparam.udnagrl,
#                      'udnagrr': dparam.udnagrr,
#                      'udnagrl_mk': dparam.udnagrl_mk,
#                      'udnagrr_mk': dparam.udnagrr_mk,
                      'ipubnttwo': dparam.ipubnttwo,
                      'ipubnttworem': dparam.ipubnttworem,
                      'nameubntline': dname.nameubntline,
                      'nameubnt': dname.nameubnt,
                      'nameubntremote': dname.nameubntremote,
                      'timewritet': dtt,
                      'timewrited': dtd,
                      }
    return data

def detail_all(url):
    """Формирование данных для страницы 'Подробно'"""
    data_name = UbntModelTest.objects.get(ipubntone__iexact=url)
    textbody = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0].detail_txt
    if textbody == '':
        with open(f'/home/zarya/project/ubntserver/sell/ip{url}_detail.txt/home/zarya/project/ubntserver/sell/ip{url}_detail.txt', 'r') as f:
            text_ip = f.readlines()
    else:
        text_ip = textbody.split(' ')
#    if textbody == '':
#        with open(f'ip{url}.txt', 'r') as f:
#            text_ip = f.readlines()
#        while text_ip[0] != 'LOCAL\n':
#            del text_ip[0]
#    else:
#        text_ip = textbody.split('\n')
#        while text_ip[0] != 'LOCAL':
#            del text_ip[0]
    ulinkname = text_ip[0]  # 'HD'
    urrsname_local = text_ip[1]  # 'Debalcevo-HES'
    urrsnamey_rem = text_ip[1].split('-')  # 'Debalcevo-HES'->['Debalcevo', 'HES']
    urrsname_rem = urrsnamey_rem[1].strip() + '-' + urrsnamey_rem[0]  # 'HES-Debalcevo'
    udistance = text_ip[2] + ' ' + 'km'  # '37.779 km'
    ufprm_local = text_ip[3] + ' ' + 'MHz'  # '11253.0 MHz'
    ufprd_local = text_ip[4] + ' ' + 'MHz'  # '10723.0 MHz'
    ufprm_rem = text_ip[4] + ' ' + 'MHz'  # '10723.0 MHz'
    ufprd_rem = text_ip[3] + ' ' + 'MHz'  # '11253.0 MHz'
    uwidth = text_ip[5].split('M')[0] + ' ' + 'MHz'  # '28 MHz'
    umod = text_ip[6]  # '8x'
#    umod = umody[2] + ' ' + umody[3] + ' ' + umody[4]
    umasterslave_local_ = text_ip[7]  # 'slave'
    if umasterslave_local_ == 'master':
        umasterslave_rem = 'SLAVE'
        umasterslave_local = 'MASTER'
    elif umasterslave_local_ == 'slave':
        umasterslave_rem = 'MASTER'
        umasterslave_local = 'SLAVE'
#    umasterslave_rem = text_ip[25]  # 'master'
    uipremote = text_ip[8]  # '10.1.11.206'

    data_detail = {
        'nameubntline': data_name.nameubntline,
        'ipubntone': data_name.ipubntone,
        'nameubnt': data_name.nameubnt,
        'ipubntremote': data_name.ipubntremote,
        'nameubntremote': data_name.nameubntremote,
        'ulinkname': ulinkname,
        'urrsname_local': urrsname_local,
        'urrsname_rem': urrsname_rem,
        'udistance': udistance,
        'ufprm_local': ufprm_local,
        'ufprd_local': ufprd_local,
        'ufprm_rem': ufprm_rem,
        'ufprd_rem': ufprd_rem,
        'uwidth': uwidth,
        'umod': umod,
        'umasterslave_local': umasterslave_local,
        'umasterslave_rem': umasterslave_rem,
        'uipremote': uipremote
    }
    return data_detail


def statl(periodurl):
    """Формирует данные для отображения на странице статистики локального IP адреса"""
    # periodurl представляет из себя строку '10.1.11.206_24'
    # отделяем IP адрес от периода
#    global data, tm
    url = periodurl.split('_')[0]
    period = int(periodurl.split('_')[1])

    # ----------------Это просто чтобы не забыть----------------------------------------
    # получаем самую последнюю запись
    #    timedata = DataUbntall.objects.filter(ipubnttwo=url).order_by('timewrite')[0]
    # ----------------------------------------------------------------------------------
    # Получаем какой минимальный уровень приёма запрограммирован (по умолчанию -90)
    prmlevel = UbntModelTest.objects.get(ipubntone=url).prm_level_for_stat

    # В функции data_ready() производится удаление записей из таблицы БД DataUbntall
    # записей старше 96 часов поэтому в переменной data96 будут только записи за 96 часов
    data96 = DataUbntall.objects.filter(ipubnttwo=url)
    # Определяем колличество записей за 96 часов
    dl96 = len(data96)
    # Получаем за 72 часа
    dl72 = round(dl96 * 3 / 4)
    # Получаем за 48 часов
    dl48 = round(dl96 / 2)
    # Получаем за 24 часа
    dl24 = round(dl96 / 4)
    # Получаем за 16 часов
    dl16 = round(dl96 / 8)

    if period == 16:
        data = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0:dl16]
        tm = 'часов'
    elif period == 24:
        data = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0:dl24]
        tm = 'часа'
    elif period == 48:
        data = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0:dl48]
        tm = 'часов'
    elif period == 72:
        data = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')[0:dl72]
        tm = 'часа'
    elif period == 96:
        data = DataUbntall.objects.filter(ipubnttwo=url).order_by('-timewrite')
        tm = 'часов'
    dataname = UbntModelTest.objects.get(ipubntone__iexact=url)
    dd = {'data': data, 'dataname': dataname, 'period': period, 'tm': tm, 'prmlevel': prmlevel}
    return dd


def statr(periodurl):
    """Формирует данные для отображения на странице статистики удалённого IP адреса"""
    # periodurl представляет из себя строку '10.1.11.206_24'
    # отделяем IP адрес от периода
#    global data, tm
    url = periodurl.split('_')[0]
    period = int(periodurl.split('_')[1])

    #    timedata = DataUbntall.objects.filter(ipubnttworem=url).order_by('-timewrite')[0]

    prmlevel = UbntModelTest.objects.get(ipubntremote=url).prm_level_for_stat

    data96 = DataUbntall.objects.filter(ipubnttworem=url)
    dl96 = len(data96)
    dl72 = round(dl96 * 3 / 4)
    dl48 = round(dl96 / 2)
    dl24 = round(dl96 / 4)
    dl16 = round(dl96 / 8)

    if period == 16:
        data = DataUbntall.objects.filter(ipubnttworem=url).order_by('-timewrite')[0:dl16]
        tm = 'часов'
    elif period == 24:
        data = DataUbntall.objects.filter(ipubnttworem=url).order_by('-timewrite')[0:dl24]
        tm = 'часа'
    elif period == 48:
        data = DataUbntall.objects.filter(ipubnttworem=url).order_by('-timewrite')[0:dl48]
        tm = 'часов'
    elif period == 72:
        data = DataUbntall.objects.filter(ipubnttworem=url).order_by('-timewrite')[0:dl72]
        tm = 'часа'
    elif period == 96:
        data = DataUbntall.objects.filter(ipubnttworem=url).order_by('-timewrite')
        tm = 'часов'
    #    data = DataUbntall.objects.filter(ipubnttworem=url)
    dataname = UbntModelTest.objects.get(ipubntremote__iexact=url)
    dd = {'data': data, 'dataname': dataname, 'period': period, 'tm': tm, 'prmlevel': prmlevel}
    return dd
