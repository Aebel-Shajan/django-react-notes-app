# Django React Notes Web App
I followed the tutorial below to create a full stack web application with user authentication using django and react. 

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/c-QsfbznSXI/0.jpg)](https://www.youtube.com/watch?v=c-QsfbznSXI)

I then deployed the site using choreo: [website preview](https://84e54057-2113-4e7e-b7be-b678a6e259ed.e1-eu-north-azure.choreoapps.dev/).
If you can't login, it may be because the database is down. Message me if you wanna access it (I have to restart the database manually haha)

# Instructions
Go to https://84e54057-2113-4e7e-b7be-b678a6e259ed.e1-eu-north-azure.choreoapps.dev/
![image](https://github.com/Aebel-Shajan/django-react-notes-app/assets/67755450/f8ea3c6d-2872-4f34-8a3d-1a1fb854a426)
Register by going to /register
![image](https://github.com/Aebel-Shajan/django-react-notes-app/assets/67755450/331e17ef-2452-4176-babe-8c5902ac09c6)
Login by going to /login
![image](https://github.com/Aebel-Shajan/django-react-notes-app/assets/67755450/f7c78fae-3697-4567-98ab-1bd19259d441)

# Key take aways
* Configure database if settings.py in the backend.
* Authentication is hard and you should leave it to django.
* Still a bit unsure on handling views and stuff for the backend. (revisit)
* Use vite and its folder structure.
* User sessions are handled using jwt tokens on the frontend in a file called api.js .
* Deploying isn't that bad.
