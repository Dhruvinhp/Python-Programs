from django.db import models

# makemigrations- create the changes and store in file
# migrate- apply the pending changes which is done by makemigrations

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):  # for print users name in contact name in admin penal
        return self.name
