from django.db import models


class user_model(models.Model):

    username=models.CharField( max_length=50,null=True)
    password=models.IntegerField(default=0)
    age=models.IntegerField(default=0)
    email=models.EmailField(max_length=254)


    def __str__(self):
        return self.username+" "+self.age
