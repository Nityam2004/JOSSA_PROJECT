from django.db import models

class College(models.Model):
    college_name = models.CharField(max_length=100)
    branch = models.CharField(max_length=100)
    unknown = models.CharField(max_length=100)  # Adjust field type based on your data
    category = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    opening_rank = models.IntegerField()
    closing_rank = models.IntegerField()

    def __str__(self):
        return self.college_name
