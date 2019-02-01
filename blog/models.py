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

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:80]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')


# Create add the blog app to settings


# Create a migration

# Migrate

# add to the admin



