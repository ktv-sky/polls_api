# Polls API project

## Running this project locally
1. Clone or download this repo
2. Set up the virtual environment
3. Run the following commands:
    ```
    pip3 install -r requirements.txt
    python3 manage.py makemigrations
    python3 manage.py migrate
    python3 manage.py createsuperuser
    python3 manage.py runserver
    ```
4. Open admin site http://127.0.0.1:8000/admin/ and create a few test objects of each type
5. Open http://127.0.0.1:8000/api/polls/
6. API Schema http://127.0.0.1:8000/api/swagger-docs/
7. API Docs http://127.0.0.1:8000/api/docs/

### Screenshots
![img1](https://i.imgur.com/LIfFeSl.png)
![img2](https://i.imgur.com/O8q8J2e.png)
