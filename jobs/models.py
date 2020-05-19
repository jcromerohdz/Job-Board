from django.db import models

class JobOffer(models.Model):
    company_name = models.CharField(max_length=60)
    company_email = models.CharField(max_length=60)
    job_title = models.CharField(max_length=60)
    salary = models.IntegerField()
    city = models.CharField(max_length=60)
    state = models.CharField(max_length=60)
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.company_name} {self.job_title}"