from django.db import models

class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='project_images/')
    link=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title
class Skill(models.Model):
    name=models.CharField(max_length=100)
    profeciency=models.IntegerField(help_text="enter from 1-100")

    def __str__(self):
        return self.name
            
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"            

class CV(models.Model):
    name = models.CharField(max_length=100, default="My CV")
    file = models.FileField(upload_to='cv/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Testimonials(models.Model):
    name=models.CharField(max_length=100)
    position=models.CharField(max_length=100,blank=True,null=True)
    feedback=models.TextField()
    image=models.ImageField(upload_to='testmonials/',blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    