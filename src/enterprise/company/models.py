from django.db import models

class Position(models.Model):
    """
    Description: Position in the company
    """
    created = models.DateTimeField(auto_now_add=True)
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    jobDescription = models.TextField(blank=True)

    class Meta:
        odering = ('name',)