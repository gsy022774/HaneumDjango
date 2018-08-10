from django.db import models

# Create your models here.
class Company(models.Model):
    company_name = models.CharField(max_length=20)
    company_no = models.IntegerField()
    
    def __str__(self):
        return self.company_no, self.company_name
    
class Report(models.Model):
    company_no = models.ForeignKey(Company, on_delete=models.CASCADE)
    report_year = models.IntegerField()
    
    def __str__(self):
        return self.company_no, self.company_year