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

## Local Development 

```
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py runserver
```
