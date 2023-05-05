from django.db import models

class Device(models.Model):
    device_name = models.CharField(max_length=50)
    device_serial = models.CharField(max_length=100, blank = True, default = '')
    device_status_id = models.CharField(max_length=5, blank = True, default = '')

    def __str__(self):
        return self.device_name

    class Meta:
    	verbose_name = 'Устройство'
    	verbose_name_plural = 'Устройство'

class Product(models.Model):
    time_created = models.DateTimeField(auto_now_add=True)
    title_product = models.CharField(max_length=50, blank = True, default = '')
    descr_product = models.CharField(max_length=180, blank = True, default = '')
    device_name = models.ForeignKey('Device', related_name='productes', on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.device_name))

    class Meta:
    	verbose_name = 'Продукт'
    	verbose_name_plural = 'Продукты'

class Status(models.Model):
    battery_status = models.CharField(max_length=50, blank = True, default = '')
    wifi_status = models.CharField(max_length=180, blank = True, default = '')
    charg_status = models.CharField(max_length=180, blank = True, default = '')
    device_name = models.ForeignKey('Device', related_name='status', on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.device_name))

    class Meta:
    	verbose_name = 'Статус'
    	verbose_name_plural = 'Статус'


