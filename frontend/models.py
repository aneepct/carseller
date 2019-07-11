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


class UserContactRequest(models.Model):
    car_body_sub_type = models.CharField(max_length=255, null=True)
    car_body_type = models.CharField(max_length=255, null=True)
    car_brand = models.CharField(max_length=255, null=True)
    car_model = models.CharField(max_length=255, null=True)
    car_type = models.CharField(max_length=255, null=True)
    car_year = models.CharField(max_length=255, null=True)
    kilometer = models.CharField(max_length=255, null=True)
    user_email = models.CharField(max_length=255, null=True)
    user_message = models.CharField(max_length=255, null=True)
    vehicle_type = models.CharField(max_length=255, null=True)
    user_address = models.CharField(max_length=255, null=True)
    user_firstname = models.CharField(max_length=255, null=True)
    user_lastname = models.CharField(max_length=255, null=True)
    user_phone = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'user_contact_requests'

    def __str__(self):              # __unicode__ on Python 2
        return str(self.user_email)
