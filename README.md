# Dodo

A open source social media to share your doo-doo's with friends and family.

### How to run locally

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