### Usage : 

    git clone https://github.com/ssoad/django_task.git
    cd django_task
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver


### For Background Task (Scheduled Transaction)

    python manage.py process_tasks
N.B: Need to run this command parallelly with server 


## Urls :
### Authentication

Register:    http://localhost/accounts/register/

Login:   http://localhost/accounts/login/    

Get User Info:   http://localhost/accounts/user

### Transactions

Send Money:  http://localhost/transaction/sendmoney/

Send Money:  http://localhost/transaction/history/

<br>

## For Details Check API Documentantion [Check Here](https://documenter.getpostman.com/view/11726924/UzJFuy59)