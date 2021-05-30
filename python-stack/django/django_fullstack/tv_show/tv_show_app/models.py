from django.db import models

class showManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["name"] = "Blog name should be at least 2 characters"
        if len(postData['network']) < 3:
            errors["desc"] = "Blog description should be at least 3 characters"
        if len(postData['release_date']) < 10:
            errors["release_date"] = "Release Date must be a full, valid date (ex. 05/17/2020)"
        if len(postData['description']) < 10:
            errors["desc"] = "Blog description should be at least 10 characters"
        return errors


class shows(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    released_date= models.DateField()
    description=models.CharField(max_length=255)
    created_at=models.DateField(auto_now_add=True)
    ubdated_at=models.DateTimeField(auto_now_add=True)  
    objects = showManager()



    

