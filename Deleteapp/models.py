from django.db import models
# Create your models here.
class delete(models.Model):
    student=models.CharField(max_length=155)
    sno=models.IntegerField(primary_key=True)
    classroom=models.IntegerField()
    def __str__(self):
        return self.student
    class Meta:
        db_table='helo'
        managed=True      