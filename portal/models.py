from django.db import models

# Create your models here.

class persoinfo(models.Model):
    id=models.AutoField(primary_key=True)
    SL=models.IntegerField(null=True)
    Name=models.CharField(max_length=200, null=True, default='')
    Contactno=models.CharField(max_length=200, null=True, default='')
    Email=models.CharField(max_length=200, null=True,default='')
    DateofBirth=models.CharField(max_length=200, null=True, default='')
    Gender=models.CharField(max_length=200,null=True, default='')
    Department=models.TextField(null=True, default='')
    Projectname=models.CharField(max_length=2000, null=True, default='')
    Painpoints=models.TextField(null=True, default='')
    Solution=models.TextField(null=True, default='')
    Innovation=models.TextField(null=True, default='')
    Features=models.TextField(null=True, default='')
    Customers=models.TextField(null=True, default='')
    Availability=models.TextField(null=True, default='')
    Businessmodel=models.TextField(null=True, default='')
    Projectdomain=models.CharField(max_length=2000, null=True, default='')
    Specifications=models.CharField(max_length=2000, null=True, default='')
    Teamdetails=models.CharField(max_length=2000, null=True, default='') 

class memberdets(models.Model):
    member_id=models.AutoField(primary_key=True)
    project_id = models.IntegerField(null=True)
    MemberName=models.CharField(max_length=200, null=True, default='')
    Contactnumber=models.CharField(max_length=200, null=True, default='')
    Email=models.CharField(max_length=200, null=True,default='')
    DateofBirth=models.CharField(max_length=200, null=True, default='')
    Gender=models.CharField(max_length=200,null=True, default='')
    Department=models.TextField(null=True, default='')
    Role=models.TextField(null=True, default='')
    Competency=models.TextField(null=True, default='')

class newuserdets(models.Model):
    id=models.AutoField(primary_key=True)
    SL=models.IntegerField(null=True)
    firstname=models.CharField(max_length=200, null=True, default='')
    lastname=models.CharField(max_length=200, null=True, default='')
    username=models.CharField(max_length=200, null=True, default='')
    emailaddress=models.CharField(max_length=200, null=True, default='')
    password=models.TextField(null=True, default='')

class documentuploadss(models.Model):
    id=models.AutoField(primary_key=True)
    SL=models.IntegerField(null=True)
    files=models.FileField(null=True, default='')

