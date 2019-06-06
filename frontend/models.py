from django.db import models

# Create your models here.


class CarBrand(models.Model):
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'car_brands'

    def get_models(self):
        return CarModel.objects.filter(car_brand=self)

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)


class CarModel(models.Model):
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'car_models'

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)


class CarYear(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'car_years'

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)


class CarDesign(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'car_designs'

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)


class CarTrim(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'car_trims'

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)


class CarType(models.Model):
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'car_types'

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)
