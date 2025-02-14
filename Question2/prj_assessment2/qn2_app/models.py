from django.db import models

# Create your models here.
class QuestionPaper(models.Model):
    subject = models.CharField(primary_key=True,max_length=100)
    qn_no = models.IntegerField()
    question = models.TextField()

    def __str__(self):
        return self.subject
