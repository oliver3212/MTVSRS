## EC2 NGINX Setup 

Install NGINX and the official Ansible role through yum 

```
sudo yum -y install python-pip
pip install ansible 
ansible-galaxy install nginxinc.nginx
```

Clone this repo, which includes playbook.yml, then run: 

```
ansible-playbook playbook.yml
```

## Local Development 

```
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
