from django.db import models

class UbntModelTest(models.Model):
    objects = None
    ipubntone = models.CharField(max_length=50, verbose_name='IP адрес РРС')
    nameubnt = models.CharField(max_length=50, verbose_name='Имя РРС')
    nameubntline = models.CharField(max_length=100, verbose_name='Название РРЛ')
    statonoff = models.BooleanField(verbose_name='Включение/Выключение мониторинга РРЛ')
    ipubntremote = models.CharField(max_length=50, verbose_name='IP адрес РРС (remote)')
    nameubntremote = models.CharField(max_length=50, verbose_name='Имя РРС (remote)')
    prm_level = models.IntegerField(default=-90, verbose_name='Минимальный уровень приёма РРС')
    prm_level_for_stat = models.IntegerField(default=-90, verbose_name='Минимальный уровень приёма РРС (Статистика)')
    distributed_system_onoff = models.BooleanField(default=False, verbose_name='Если "v" - IP-адрес взят в мониторинг распределённой системой (Не заполнять!!! Поле только для чтения)')
    numberubntline = models.CharField(max_length=50, verbose_name='Номер РРЛ')
    class Meta:
        verbose_name_plural = 'IP адреса РРС'
        verbose_name = 'IP адрес РРС'

    def __str__(self):
        return self.ipubntone

class DataUbntall(models.Model):
    objects = None
    udprml0 = models.IntegerField(verbose_name='Уровень приёма(0) локального РРС')
    udprml1 = models.IntegerField(verbose_name='Уровень приёма(1) локального РРС')
    udprmr0 = models.IntegerField(verbose_name='Уровень приёма(0) удалённого РРС')
    udprmr1 = models.IntegerField(verbose_name='Уровень приёма(1) удалённого РРС')
    udspeedl = models.FloatField(verbose_name='Емкость приёма локального РРС')
    udspeedr = models.FloatField(verbose_name='Емкость приёма удалённого РРС')
    ipubnttwo = models.CharField(max_length=50)
    ipubnttworem = models.CharField(max_length=50)
    mistake_ip = models.CharField(max_length=1000)
    detail_txt = models.CharField(max_length=5000)
    timewrite = models.DateTimeField(auto_now_add=True, verbose_name='Записано')
    
    def __str__(self):
        return self.ipubnttwo

    class Meta:
        verbose_name_plural = 'Уровень приёма локального РРС'
        verbose_name = 'Уровень приёма локального РРС'
        ordering = ['-timewrite']

class Startprocess(models.Model):
    startproc = models.BooleanField(default=False, verbose_name='Старт/Стоп Selenium')

    class Meta:
        verbose_name_plural = 'Старт/Стоп Selenium'
        verbose_name = 'Старт/Стоп Selenium'

class Listipubnt(models.Model):
    objects = None
    current_list_ip = models.CharField(max_length=1000)

#class Listurl(models.Model):
#    number_one = models.CharField(max_length=50, default='', verbose_name='Первый IP')
#    number_two = models.CharField(max_length=50, default='', verbose_name='Второй IP')
#    number_three = models.CharField(max_length=50, default='', verbose_name='Третий IP')
#    number_four = models.CharField(max_length=50, default='', verbose_name='Четвёртый IP')
#    number_five = models.CharField(max_length=50, default='', verbose_name='Пятый IP')
#    number_six = models.CharField(max_length=50, default='', verbose_name='Шестой IP')
#    number_seven = models.CharField(max_length=50, default='', verbose_name='Седьмой IP')
#    number_eight = models.CharField(max_length=50, default='', verbose_name='Восьмой IP')
#    number_nine = models.CharField(max_length=50, default='', verbose_name='Девятый IP')
#    number_ten = models.CharField(max_length=50, default='', verbose_name='Десятый IP')
#    number_eleven = models.CharField(max_length=50, default='', verbose_name='Одиннадцатый IP')
#    number_twelve = models.CharField(max_length=50, default='', verbose_name='Двенадцатый IP')
#    number_thirteen = models.CharField(max_length=50, default='', verbose_name='Тринадцатый IP')
#    number_fourteen = models.CharField(max_length=50, default='', verbose_name='Четырнадцатый IP')
#    number_fifteen = models.CharField(max_length=50, default='', verbose_name='Пятнадцатый IP')
#    number_sixteen = models.CharField(max_length=50, default='', verbose_name='Шестнадцатый IP')


class AutoRestart(models.Model):
    objects = None
    schetchik = models.IntegerField()
    firstid = models.IntegerField()	

