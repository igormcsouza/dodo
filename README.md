# Dodo

A open source social media to share your doo-doos with friends and family.

## How to use?

You must first Register (/register) and then login to the application. Once
logged, you can write your own doo-doos or share others doo-doos.

## Developing it

### Making Changes to the database

Every change on database must be migrate before being available to the user.
First make sure the database and the migration folder is created already, if
that is not the case, just create it with th command bellow.

```bash
dodo$ flask db init
```

Update the database by running the following commands.

```bash
dodo$ flask db migrate -m "message"
dodo$ flask db upgrade
```

If you have any problems, refer to the
[migrate documentation](https://flask-migrate.readthedocs.io/en/latest/) which
is prepared to help in any issue related.

__NOTE:__ In order to update the tables, I needed to import them at the file
where I build the app, I'm still not sure why this is needed, but is there.

### Running it locally

If you prefer, you can run the project locally in your computer, just follow the
steps bellow and all should be done.

First install the dependencies on the virtual environment you should have
created already.

```bash
dodo$ pip install -r requirements.txt
```

Then, run the project using **gunicorn**, like on the command below. In
production, the `--reload` flag is not needed, that is intent only for
development purposes.

```bash
dodo$ gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app --reload
```

There is also a Docker option, first make sure you have docker and
docker-compose installed, follow the command bellow.

```bash
dodo$ docker-compose build
dodo$ docker-compose up -d
```
