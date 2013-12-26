music_album
===========

Music Catalog is a Django project in which user will be able to see the songs,albums,artists and create there playlist.
-----------

Requirements :
Python
Django
Twitter bootstrap south

Django project that will manage the store the music tracks and allow user to create their playlist

## Getting Started

These instructions are for Unix/OS X, you will have to modify these a bit to get going on Windows.
#### 1. Check out the repository:

```
  git clone git://github.com/param107/music_album
  cd music_album
```
Change settings.py and set ur systems path in Database and Template Dir

Twitter bootstrap is being used for designing part. Install the toolkit for the same.
sudo pip install django south django-bootstrap-toolkit

Initialize our database

python manage.py syncdb
 
Start the server:

python manage.py runserver

You should now be able to see the songs, and select and add songs to your playlist.
