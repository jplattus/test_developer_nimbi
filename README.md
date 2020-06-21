# Nimbi Test - Jean Pierre Lattus

This is a project created with Django as a API REST host backend and Vue.js as a frontend framework. 
It will be used to help Nimbi to HR selection process to evaluate the job applicant Jean Pierre Lattus for Full-Stack Developer position. 

It's a simple blog, with basic CRUD operations that register user activity.

## Frontend Prerequisites
* Your prefered browser
* npm (tested with v6.14)
* node (tested with v14.4.0)

## Backend Prerequisites
* python 3.6+
* virtualenv 

## Some technologies and libraries used in this project

* [Django](https://vuejs.org): Python web framework
* [Django Rest Framework](https://www.django-rest-framework.org): Django REST framework is a powerful and flexible toolkit for building Web APIs.
* [Pytest](https://docs.pytest.org/): Python test framework.
* [Vue.js](https://vuejs.org): Javascrypt framework
* [Vue-cli3](https://cli.vuejs.org):  Standard Tooling for Vue.js Development
* [Vue-router](https://router.vuejs.org): Routing. Helps to integrates the Vue.js core to build Single Page Applications
* [Axios](https://github.com/axios/axios): Promise based HTTP client for the browser and node.js
* [Vuex](https://vuex.vuejs.org): It serves as a centralized store for all the Vue components in an application
* [Vue-chart.js](https://vue-chartjs.org): Easy and beautiful charts with Chart.js and Vue.js.
* [CoreUI Pro](https://coreui.io): Bootstrap Admin Template
* [Boostrap4](https://getbootstrap.com/docs/4.5/getting-started/introduction/): The world's most popular framework for building responsive, mobile-first sites.
* [Bootstrap-Vue](https://bootstrap-vue.org): Integration with bootstrap4 and Vue.js
* And of course Javascript, HTML and CSS

## Backend Instalation


``` bash
# Create a python3 virtual enviorement
$ virtualenv -p python3 nimbi 

# cd into created folder#
$ cd nimbi

# Make a directory to put the repository. Ej. src/
$ mkdir src

# clone the repo
$ git clone https://github.com/jplattus/test_developer_nimbi.git src/

# Activate virtual env and install python dependencies
$ source bin/activate
$ cd src/
$ pip install -r requirements.txt

### IMPORTANT ###
# Create a postgres database and update project settings with your credentials
# We will be using local.py settings as we didnt need productions settings
# Setting file is in: src/test_developer_nimbi/settings/local.py

# Migrate the project apps to the database and create superuser.
$ python manage migrate
$ python manage.py createsuperuser 
``` 

## Backend Usage

Serve the backend webservices by hosting a local server

`python manage.py runserver`

You are good to go. Install and run the frontend to finish

## Frontend Installation

``` bash
$ cd frontend

# install app's dependencies
$ npm install
```

## Frontend  Usage

``` bash
# serve with hot reload at localhost:8080
npm run serve

### At this point you can test the app on your local server. ###

# (Deployment) use build for production with minification when deploying
npm run build

```


## Frontend Relevant folders and files tree

```
frontend/
├── babel.config.js
├── jest.config.js
├── package-lock.json
├── package.json                    # build scripts and dependencies
├── public                          # pure static assets (directly copied)
├── src                             # project root
│   ├── App.vue                     # main app component
│   ├── _nav.js                     # navigation items json
│   ├── assets                      # module assets (processed by webpack)
│   ├── containers                  # ui containers
│   ├── main.js                     # app entry file
│   ├── router                      # vue-router
│   ├── store                       # vuex
│   └── views                       # ui views
└── vue.config.js                   # vue cli config
```

## Last considerations
I would have liked to use Google Analytics API, but the documentation is very long for the 
short time i have to deevlop this project.

Also, not proud about dashboard as it could be a lot better. I wasted a lot of time trying to understand GA API.

Didnt have time test driven develop. I'm really sorry.

Anyway, I really hope you like this test, and overall can be useful for you.

Please contact me if you have troubles installing the app.

Regards!

## Creator
Jean Pierre Lattus
* [LinkedIn](https://www.linkedin.com/in/jeanpierrelattus/)
* [GitHub](https://github.com/jplattus) (Not much interesting public repos to see)
