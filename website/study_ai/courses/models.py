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
    description = models.TextField()
    def __str__(self):
        return str(self.course_number)

class Achievment(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=100)
    requirements = models.CharField(max_length=500)
    requirements_json_path = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)

class Major(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    name = models.CharField(max_length=200)
    webpage = models.CharField(max_length=200)
    requirements = models.ManyToManyField(Achievment)
    def __str__(self):
        return str(self.name)

class User(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    current_courses = models.ManyToManyField(Course, related_name='current_courses') 
    past_courses = models.ManyToManyField(Course, related_name='past_courses') 
    grades = models.CharField(max_length=2) # better way 

class Group(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    group_members = models.ManyToManyField(User) 

