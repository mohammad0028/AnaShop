# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class IranOstan(models.Model):
    name = models.CharField(max_length=255)
    amar_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'iran_ostan'

    def __str__(self):
        return self.name


class IranShahr(models.Model):
    name = models.CharField(max_length=255)
    shahr_type = models.IntegerField(blank=True, null=True)
    # ostan = models.IntegerField(blank=True, null=True)
    ostan = models.ForeignKey(IranOstan, null=True, on_delete=models.CASCADE)
    shahrestan = models.IntegerField(blank=True, null=True)
    bakhsh = models.IntegerField(blank=True, null=True)
    amar_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        db_table = 'iran_shahr'

    def __str__(self):
        return self.name
