from django.db import models

# Create your models here.


class City(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)
    area = models.CharField(max_length=255, null=True)
    partner = models.CharField(max_length=255, null=True)
    lat = models.FloatField()
    lng = models.FloatField()
    
    class Meta:
        db_table = 'cities'

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)


class HomepageContent(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contents = models.TextField(null=True)
    
    class Meta:
        db_table = 'homepage_contents'

    def __str__(self):              # __unicode__ on Python 2
        return str(self.name)


class CityPage(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contents = models.TextField(null=True)

    class Meta:
        db_table = 'citypage_contents'

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class StepOne(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contents = models.TextField(null=True)

    class Meta:
        db_table = 'stepone_contents'

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class StepTwo(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contents = models.TextField(null=True)

    class Meta:
        db_table = 'steptwo_contents'

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)


class StepThree(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    contents = models.TextField(null=True)

    class Meta:
        db_table = 'stepthree_contents'

    def __str__(self):  # __unicode__ on Python 2
        return str(self.name)
