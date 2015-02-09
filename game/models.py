from django.db import models

# Create your models here.
class HelpText(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

# Create your models here.
class Problem(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField(default="Put your problem here")
    actual_result = models.TextField(default="What happend in reallife")
    background_media_url = models.CharField(max_length=200)
    actual_result_media_url = models.CharField(max_length=200)
    actual_result_source = models.TextField(default="Put your source here")
    event_date = models.DateTimeField(auto_now_add=True, blank=True)
    actual_result_title = models.CharField(max_length=200)
    tweet = models.CharField(max_length=200)
    tweet_link = models.CharField(max_length=255)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.name

class Choice(models.Model):
    problem = models.ForeignKey(Problem)
    text = models.CharField(max_length=255)
    resultText = models.TextField(default="This is the resolution text")
    scoreA = models.FloatField(default=1.0)
    scoreB = models.FloatField(default=1.0)
    scoreC = models.FloatField(default=1.0)
    scoreD = models.FloatField(default=1.0)
    scoreE = models.FloatField(default=1.0)
    scoreF = models.FloatField(default=1.0)
    def __unicode__(self):  # Python 3: def __str__(self):
        return self.problem.name +": "+ self.text