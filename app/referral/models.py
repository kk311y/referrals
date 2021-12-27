from django.db import models

# Create your models here.
class Participant(models.Model):
    last_name = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True)
    date_of_birth = models.DateField()

class Program(models.Model):
    program_name = models.CharField(max_length=100, blank=False, null=False)
    organization = models.CharField(max_length=100, blank=True)
    street_address = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    zip_code = models.CharField(max_length=9)


class Staff(models.Model):
    last_name = models.CharField(max_length=50, blank=False, null=False)
    first_name = models.CharField(max_length=50, blank=False, null=False)
    middle_name = models.CharField(max_length=50, blank=True)
    program = models.ForeignKey(Program, on_delete=models.CASCADE)


class Referral(models.Model):
    participant = models.OneToOneField(Participant, on_delete=models.CASCADE)
    date_of_referral = models.DateTimeField(auto_now=True)
    referred_to_program = models.OneToOneField(Program, on_delete=models.CASCADE)
    referring_staff = models.OneToOneField(Staff, on_delete=models.CASCADE)


    

    #     title = models.CharField(max_length=70, blank=False, default='')
    # tutorial_url = models.CharField(max_length=200, blank=False, default='')
    # image_path = models.CharField(max_length=150, blank=True, null=True)
    # description = models.CharField(max_length=200, blank=False, default='')
    # published = models.BooleanField(default=False)