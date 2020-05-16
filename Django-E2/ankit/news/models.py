from django.db import models

# Create your models here.


class employee_details(models.Model):
	sno=models.IntegerField()
	name=models.CharField(max_length=255)
	email=models.EmailField(max_length=100)
	description=models.TextField()
	user_create_date=(models.DateTimeField(auto_now_add=True))






