from django.db import models

# Create your models here.
# Track will list the information about tracks
class Track(models.Model):
    name = models.CharField('Name', help_text='Enter the name of the Track', max_length=50)
    link = models.SlugField('Link', help_text='Unique link to Track', max_length=10)
    about = models.TextField('Description', help_text='About Track')
    is_famous = models.BooleanField('Famous', help_text='tick if famous', default= False)
    artist = models.ManyToManyField('Artist', related_name ='track_artist')
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Track'
        ordering = ['date']
    def __unicode__(self):
        return self.name

#Artist will contain information about the artist
class Artist(models.Model):
    name = models.CharField('Name', help_text='Enter the name of the Artist', max_length=50)
    link = models.SlugField('Link', help_text='Unique link to Artist', max_length=10)
    about = models.TextField('Description', help_text='About Artist')
    thumbnail = models.ImageField("Image", help_text='Uplaod Image of the Artist', upload_to='static/artist/images', default='static/artist/default.jpg')
    dob = models.DateField('DOB', help_text='Date Of Birth of Artist')
   
    is_famous = models.BooleanField('Famous', help_text='Tick if Artist is famous', default=False)

    class Meta:
        verbose_name_plural = 'Artist'
        ordering = ['name']
    def __unicode__(self):
        return self.name
    
# album will store info about albums
class Album(models.Model):
    name = models.CharField('Name', help_text='Enter the name of the Album', max_length=50)
    link = models.SlugField('Link', help_text='Unique link to Album', max_length=10)
    about = models.TextField('Description', help_text='About Album')
    track = models.ManyToManyField('Track', related_name ='track_album')# album can have many tracks
    genre = models.CharField('Genre', help_text='Enter the genre of the Album', max_length=15)
    thumbnail = models.ImageField("Image", help_text='Upload Image of the Artist', upload_to='static/album/images', default='static/album/default.jpg')
    relyr = models.DateField("Release Year", help_text='Release date of Album')
    is_famous = models.BooleanField('Famous', help_text='Tick if Album is famous', default=False)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'Album'
        ordering = ['relyr']
    def __unicode__(self):
        return self.name





