from django.db import models


class Manufacturer(models.Model):
    manufacturer_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.manufacturer_name


class HeatingModel(models.Model):
    model_name = models.CharField(max_length=200)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.model_name


class ErrorCode(models.Model):
    error_code = models.CharField(max_length=200)
    description = models.TextField()
    solution = models.TextField()
    model_name = models.ForeignKey(HeatingModel, on_delete=models.CASCADE)
    manufacturer_name = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    inserted_date = models.DateField(auto_now_add=True)
    last_modified_date = models.DateField(auto_now=True)
