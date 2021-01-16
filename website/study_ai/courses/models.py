from django.db import models

class Course(models.Model):
    """Representation of a course, not a specific course
    Args:
        models ([type]): [description]
    """
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    title = models.CharField(max_length=100)
    course_number = models.CharField(max_length=10) 
    # course_ids TODO: Add this at some point 
    prereqs = models.ManyToManyField("self")

class Achievment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    requirements = models.CharField(max_length=500)
    requirements_json_path = models.CharField(max_length=100)

class Major(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    webpage = models.CharField(max_length=200)
    requirements = models.ManyToManyField(Achievment)
