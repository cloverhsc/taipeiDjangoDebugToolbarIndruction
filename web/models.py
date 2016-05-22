from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    weight = models.IntegerField()

    def __unicode__(self):
        return unicode(self.last_name + ' ' + self.first_name)

    class Meta:
        db_table = 'user'
