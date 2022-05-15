from django.db import models
from django.forms import CharField
from numpy import True_, integer
from django.db.models import Max

# Create your models here.

class Team(models.Model):
    Team_name = models.CharField(max_length=50)
    # Team_id = models.CharField(max_length=10,null=True,default="ITSP220000")
    # Team_id = models.CharField(max_length=50, default="", editable=False)

    # Team_id = models.IntegerField(primary_key=True, editable=True)
    # Team_id = models.CharField(max_length=10)
    Team_id = models.CharField(primary_key=True, editable=True, max_length=10)
    # Team_id = models.CharField(primary_key=True, editable=True,max_length=10)
    member1 = models.CharField(max_length=50,null=True)
    member2 = models.CharField(max_length=50,default="NA")
    member3 = models.CharField(max_length=50,default="NA")
    member4 = models.CharField(max_length=50,default="NA")
    Team_info = models.URLField(max_length=200,null=True)
    def __str__(self):
        return self.Team_name + " ( " + self.Team_id + " )" 


    # def save(self, **kwargs):
    #     max = 1
    #     if not self.id:
    #         # max = Team.objects.aggregate(id_max=Max('id'))['id_max']
    #         print(Max('id'))

    #         self.id = "{}{:04d}".format('ITSP22', max if max is not None else 1)
    #         max = max + 1 
    #     super().save(*kwargs)

    # custom_id = models.IntegerField()

    # @property
    # def sid(self):
    #     return "ITSP%06d" % self.Team_id
    # def save(self, *args, **kwargs):
    #     if not self.Team_id is None:
    #         self.Team_id = ('ITSP' + str(self.Team_id))
    #     return super(Team, self).save(*args, **kwargs)