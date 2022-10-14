from django.db import models

class File(models.Model):
    transaction_type = models.CharField(max_length=255)
    date = models.CharField(max_length=255)
    amount = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    card_number = models.CharField(max_length=255)
    time = models.CharField(max_length=255)
    store_owner = models.CharField(max_length=255)
    store = models.CharField(max_length=255)

class FileUploader(models.Model):
    upload = models.FileField(upload_to="upFiles/")
    