from django.db import models

# Create your models here.

#Escalation Matrix
class EscMat(models.Model):
	oper=models.CharField(max_length=100)
	ari=models.CharField(max_length=100)
	aname=models.CharField(max_length=100)
	group_id = models.EmailField()
	person1=models.CharField(max_length=100)
	person2=models.CharField(max_length=100)
	person3=models.CharField(max_length=100)
	person4=models.CharField(max_length=100)
	
	class Meta:
		db_table="escalation"

#SOP		
class sop(models.Model):
	doc = models.CharField(max_length=100, unique=True)
	region = models.CharField(max_length=100)
	operator = models.CharField(max_length=100)
	appt = models.CharField(max_length=100)
	apname = models.CharField(max_length=100)
	topic = models.CharField(max_length=100)
	ip = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='static/pdf/sop')
	
	def __str__(self):
		return self.title
	def delete(self, *args, **kwargs):
		self.pdf.delete()
		super().delete(*args, **kwargs)
	class Meta:
		db_table = "sop"

#Training Documents
class train(models.Model):
	doc = models.CharField(max_length=100, unique=True)
	product = models.CharField(max_length=100)
	pdf = models.FileField(upload_to='static/pdf/training')
	
	def __str__(self):
		return self.title
	def delete(self, *args, **kwargs):
		self.pdf.delete()
		super().delete(*args, **kwargs)
	class Meta:
		db_table = "train"

#Shift Roster
class shift(models.Model):
	year = models.CharField(max_length=4)
	month = models.CharField(max_length=12)
	level = models.CharField(max_length=5)
	imag = models.FileField(upload_to='static/shift')
	
	def __str__(self):
		return self.title
	def delete(self, *args, **kwargs):
		self.imag.delete()
		super().delete(*args, **kwargs)
	class Meta:
		db_table = "shift"
