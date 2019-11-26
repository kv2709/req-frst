from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class RequestForsto(models.Model):
    """Set fields, what phohe magager input on talk with client"""
    car_model = models.CharField(max_length=200)
    vin = models.CharField(max_length=20)
    description = models.TextField()
    client_name = models.CharField(max_length=40)
    phone = models.CharField(max_length=10)
    date_added = models.DateTimeField(auto_now_add=True)
    res_code = models.IntegerField
    res_response = models.CharField(max_length=200)
    owner = models.ForeignKey(User)

    def __str__(self):
        """Return string value model"""
        return self.client_name + "  т." + self.phone + "   " \
               + str(self.date_added.day)+"-"+ str(self.date_added.month)\
               + "-" + str(self.date_added.year)+"  "+ str(self.date_added.hour+7)\
               + ":" + str(self.date_added.minute)\
               + " " + str(self.res_response)
