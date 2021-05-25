from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200,null=True)
    pub_date = models.DateTimeField('date published')


class Registration(models.Model):
    User_id = models.AutoField(primary_key=True)
    #id = models.CharField(max_length=200,null=True)
    supplier_business_name = models.CharField(max_length=200,null=True)
    supplier_address = models.CharField(max_length=200,null=True)
    representaive_full_name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=200, null=True)
    seondary_representaive_full_name = models.CharField(max_length=200, null=True)
    secondary_email_address = models.CharField(max_length=200, null=True)
    secondary_phone_number = models.CharField(max_length=200, null=True)
    related_entities = models.CharField(max_length=200, null=True)
    Product_and_services = models.CharField(max_length=200, null=True)

    class Meta:
        verbose_name_plural = 'Registration'

    def __unicode__(self):
        return str(self.supplier_business_name)

class user_data(models.Model):
    pr_id = models.AutoField(primary_key=True)
    User_id = models.ForeignKey(Registration, null=True, on_delete=models.CASCADE)
    supplier_business_name = models.CharField(max_length=200,null=True)
    supplier_address = models.CharField(max_length=200,null=True)
    primary_representaive_full_name = models.CharField(max_length=200,null=True)
    email_address = models.CharField(max_length=200,null=True)
    phone_number = models.CharField(max_length=200,null=True)
    seondary_representaive_full_name = models.CharField(max_length=200,null=True)
    secondary_email_address = models.CharField(max_length=200,null=True)
    secondary_phone_number = models.CharField(max_length=200,null=True)
    related_entities = models.CharField(max_length=200,null=True)
    Product_and_services = models.CharField(max_length=200,null=True)
    class Meta:
        verbose_name_plural = 'user_data'

    def __unicode__(self):
        return str(self.supplier_business_name)



