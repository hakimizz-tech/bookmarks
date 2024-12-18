# bookmark project 
This a project that users are able to bookmark images from other website.  
The user can like the images that other users bookmark and follow other users.  
The dashboard page displays the recent activities that other users have been up to

## Registering and authenticating users
I've used django-auth **_django.contib.auth_** framework to authenticate an register new users.  
We used *Google Oauth2.0* to enable user to also signup using their E-mail account.  
when users create an account django-auth framework or Google Oauth a profile for a user is created

## Profound modules that were used
I used redis to increase optimization and performance by ranking the most viewed image and retrieving the total likes of an image to avoid hiting the database everytime you want to check the number of likes an image has.

