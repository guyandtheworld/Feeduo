# HungerShack


Set up virtual enviornment by the command, 
`virtualenv env`


after getting into the virtual enviornment install the following.


Install the following dependencies, 


* `Django==1.11.2`
* `djangorestframework==3.6.3`
* `psycopg2==2.7.1`
* `requests==2.18.1`


using pip.


Javascript and angular dependencies can be found on [here](http://engineroom.trackmaven.com/blog/getting-started-drf-angularjs-part-1/)


Backend runs on postgresql, instructions to run postgresql on local system can be found at [here](https://www.digitalocean.com/community/tutorials/how-to-use-postgresql-with-your-django-application-on-ubuntu-14-04). Set the credentials accordingly and change it at the settings.py.

## How different parts fit together.

### Chain

Chain, defaultly has one entity unless more is added in the future. It is the core entity. 

* All the users are related by ManyToMany relationships to Chain.
* All the coupons are related by ManyToOne relationships to Chain.

### Users 

Users are the people we sent SMS to, consists of Name, Phone Number, email, choice of chains.

### Coupons

Coupons are related as ManyToOne relationship to Chain.