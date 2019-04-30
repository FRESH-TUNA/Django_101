# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Phonebook(models.Model):
    phonebookid = models.IntegerField(db_column='phoneBookId', primary_key=True)  # Field name made lowercase.
    name = models.TextField(blank=True, null=True)
    phonenumber = models.IntegerField(db_column='phoneNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'PhoneBook'
