# django-boiler
BoilerPlate code for django project

Instructions for setup:

	mkdir your-project-name && cd your-project-name
	git clone git@github.com:batavinash/django-boiler.git .
	python3 -m venv env
	source env/bin/activate
	pip install -r requirements.txt
	cd src
	
	touch .env
	
	Inside the .env file write
	
	SECRET_KEY=^302r_)8)4mnpxe1+o=i4lu-8!6oio=!&zuz24b2v=5!4-ec+w 
	or you can generate a new secret key using [miniwebtool](https://miniwebtool.com/django-secret-key-generator/)
	
	python manage.py rename your-project-name
