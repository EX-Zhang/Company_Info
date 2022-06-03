# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class CompanyInfo(models.Model):
    symbol = models.CharField(db_column='Symbol', primary_key=True, max_length=6)  # Field name made lowercase.
    company_name = models.CharField(db_column='Company_Name', max_length=255, blank=True, null=True)  # Field name made lowercase.
    country = models.CharField(db_column='Country', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ipo_year = models.TextField(db_column='IPO_Year', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sector = models.CharField(db_column='Sector', max_length=255, blank=True, null=True)  # Field name made lowercase.
    last_sale = models.FloatField(db_column='Last_Sale', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company_info'


class CompanyStock(models.Model):
    symbol = models.CharField(db_column='Symbol', primary_key=True, max_length=6)  # Field name made lowercase.
    date = models.DateField(db_column='Date')  # Field name made lowercase.
    open = models.FloatField(db_column='Open', blank=True, null=True)  # Field name made lowercase.
    close = models.FloatField(db_column='Close', blank=True, null=True)  # Field name made lowercase.
    high = models.FloatField(db_column='High', blank=True, null=True)  # Field name made lowercase.
    low = models.FloatField(db_column='Low', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company_stock'
        unique_together = (('symbol', 'date'),)
