from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text
    
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)  

    def __str__(self):
        return self.choice_text
    
class Client(models.Model):
    fname = models.CharField(max_length=40)
    lname = models.CharField(max_length=40)
    street_addr = models.CharField(max_length=100)
    city_name = models.CharField(max_length=40)
    state = models.CharField(max_length=40)

    def __str__(self):
        return self.fname + " " + self.lname