from django.db import models

# Create your blog model
class Blog(models.Model):
    # Title
    title = models.CharField(max_length=200)

    # Publication date
    pub_date = models.DateTimeField(max_length=255)

    # body
    body = models.TextField(max_length=200)

    # image
    image = models.ImageField(upload_to='images/')

# Create add the blog app to settings


# Create a migration

# Migrate

# add to the admin



