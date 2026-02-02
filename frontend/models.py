from django.db import models

class Main_Movie(models.Model):
    main_banner = models.ImageField(upload_to='media/')
    nomi = models.CharField(max_length=50)

    
    def __str__(self):
        return self.nomi
    

#makemigrations
#migrate

class Movie(models.Model):
    main = models.ImageField(upload_to='media/')
    nom = models.CharField(max_length=50, null=True)
    
    def __str__(self):
        return self.nom
    
class Mainn(models.Model):
    banner = models.ImageField(upload_to='media/')
    nomii = models.CharField(max_length=50, null=True)

    
    def __str__(self):
        return self.nomii