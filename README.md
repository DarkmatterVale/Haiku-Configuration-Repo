# Haiku-Configuration-Repo
A place to find information about whether your hardware configuration will work with Haiku

## Deploying to Heroku

```sh
$ heroku create --stack cedar
$ git push heroku master

$ heroku run python manage.py migrate
```