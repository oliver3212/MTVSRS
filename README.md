## EC2 and NGINX Setup 

Install esentials, NGINX, and the official Ansible role through yum 

```
sudo yum -y install git
sudo yum -y install python-pip
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

Make sure to add inbound rules for TCP:8000 in AWS, then start the NGINX service 

```
sudo systemctl start nginx
```

Generate new Django SECRET_KEY (which really is more of a *salt*..) to environment, as we shouldn't hardcode secrets.

```
echo "export SECRET_KEY='$(openssl rand -hex 40)'" > .DJANGO_SECRET_KEY
source .DJANGO_SECRET_KEY
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

## Local Development 

```
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
