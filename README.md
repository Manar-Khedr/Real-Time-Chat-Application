# Real-Time-Chat-Application

## 1. Install Required libs:
```
pip install Django
pip install channels
pip install daphne
pip install channels_ws
```

## 2. Download the project.
## 3. Open the real_time_chat folder.
## 4. Activate the virtual environment:
```
virtualenv django_env 
source django_env/bin/activate
```
## 5. Run the manage.py file to start the project:
```
python manage.py runserver  
```

## 6. Click on the localhost address provided in your terminal. For example:
```
Starting ASGI/Daphne version 4.0.0 development server at http://127.0.0.1:8000/
```
## 7. You will be brought up to the Home page, click on the Sign-Up button to create an account.
<img width="1792" alt="Screen Shot 2023-11-30 at 12 56 35 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/05bb0061-8f66-4bd5-9fcd-3a396defaa98">

## 8. Log-in in with your username and password.
## 9. Choose your desired room to start chatting!
<img width="1792" alt="Screen Shot 2023-11-30 at 12 59 09 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/638a6ef9-d2f0-44fc-9bc2-241a71c85160">
<img width="1792" alt="Screen Shot 2023-11-30 at 1 00 52 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/a554407a-8cf0-4bc5-9694-22a6266383dd">

## 10. To Upload a file, simply click on the 📎 button and upload your file, then go back to the chatting room.
<img width="1792" alt="Screen Shot 2023-11-30 at 1 02 05 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/f0bfd3e2-7a83-47a5-a4c5-d0c0379fb294">

## 11. To view and download the uploaded file, click on the Media button above.
<img width="1792" alt="Screen Shot 2023-11-30 at 1 03 36 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/8e8009fb-4c09-4eb0-b0a3-6bf47d3a03da">

## 12. To add rooms to the application, write the following commands first to create an admin account:
```
python manage.py createsuperuser 
```

## 13. Open the following URL, and login using the admin account information:
http://127.0.0.1:8000/admin/

## 14. Click on the "+" next to rooms to create a new room.
<img width="1061" alt="Screen Shot 2023-11-30 at 1 08 32 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/1e39760a-99c8-46ff-a32b-5259810b6277">
<img width="928" alt="Screen Shot 2023-11-30 at 1 09 45 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/4d59a5dd-9fc2-4e7d-b27c-e8949866648b">

## 15. Go back to the rooms page, where you will find the new room added!
<img width="1790" alt="Screen Shot 2023-11-30 at 1 10 58 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/4373dadd-1102-4b93-987f-4174d61cf09a">

## 16. To view who is currently active in which room, view the terminal:
<img width="565" alt="Screen Shot 2023-11-30 at 1 12 53 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/ebe614f2-c06a-4d5e-bf42-cc9d09349293">
<img width="1792" alt="Screen Shot 2023-11-30 at 1 13 24 PM" src="https://github.com/Manar-Khedr/Real-Time-Chat-Application/assets/77106419/c13e7776-9779-470f-acd0-54a9ca8ff3c9">
