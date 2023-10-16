from django.db import models

class warehouse(models.Model):
    item = models.CharField(max_length=200)
    quantity = models.IntegerField()
    createdDate = models.DateTimeField(auto_now_add=True)
    LastModified = models.DateTimeField(auto_now_add=True)
    WarehouseId =  models.CharField(max_length=200)

    def __str__(self):
        return self.item
    
# class File(models.Model):
#     file = models.FileField(upload_to="files")

class Archivo(models.Model):
    nombre = models.CharField(max_length=255)
    archivo = models.FileField(upload_to='files/')
    fecha_subida = models.DateTimeField(auto_now_add=True)
