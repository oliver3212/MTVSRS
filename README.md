## EC2 and NGINX Setup 

Install essentials, NGINX, MariaDB (mostly to provide mysql_config which is used by mysqlclient package for Django's connector) and the official Ansible role

```
sudo yum -y install git python-pip mariadb105-devel gcc python3.9-devel
pip install ansible 
ansible-galaxy install nginxinc.nginx
```

Clone this repo, which includes playbook.yml, then run: 

```
git clone https://github.com/CPSC5071/mtvsrs.git
ansible-playbook playbook.yml
```

Make changes to /etc/nginx/nginx.conf to redirect to port 8000, use the file in repo. 

(Not best practice, should modularize configs in conf.d/)

```
sudo cp nginx.conf ~/etc/nginx/nginx.conf
```

Enable (or just start) the NGINX service 

```
sudo systemctl enable nginx
```

Generate new Django SECRET_KEY (which really is more of a *salt*..) to environment, as we shouldn't hardcode secrets.

```
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
```

Change the password in settings.py

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "mm_team06_01",
        'USER': 'admin',
        'PASSWORD': '<INSERT PASSWORD HERE>',
        'HOST': 'cpsc5071.cnsskm04otsd.us-east-1.rds.amazonaws.com',
        'PORT': '3306',
    }
}
```

Start Django app as a background process

```
pip install -r requirements.txt
python3 manage.py migrate
nohup python3 manage.py runserver &
```

NOTE: 

In a real prod scenario, we shouldn't be using Django's default web server, use something like Gunicorn instead (https://docs.djangoproject.com/en/3.2/ref/django-admin/#runserver)

> DO NOT USE THIS SERVER IN A PRODUCTION SETTING. It has not gone through security audits or performance tests.
> (And that’s how it’s gonna stay. We’re in the business of making Web frameworks, not Web servers, so improving this
> server to be able to handle a production environment is outside the scope of Django.)

## Pulling changes and connecting to EC2 

After new changes have been merged to main branch, we need to SSH to our EC2 and pull the changes.

Ask Devin for pem file.

```
ssh -i devin.pem ec2-user@3.85.11.137
cd mtvsrs 
git pull 
```

Restart the server

```
source .DJANGO_SECRET_KEY
kill $(ps aux | grep "[p]ython3 manage.py runserver" | head -n 1 | awk '{print $2}')
python3 manage.py migrate
nohup python3 manage.py runserver &
```

## Local Development 

Set mtvsrs/settings.py DEBUG = True, then: 

```
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
