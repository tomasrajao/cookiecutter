Cookiecutter
===================

~~~~
Configurações
~~~~
AWS:
    AWS_IAM_::

        Marcar "Chave de acesso: acesso programático"

    AWS_S3_::
.. image:: https://i.imgur.com/DwZzJDo.png
   :name: S3 Policy Gen
   :align: center
   :alt: S3 Policy Gen
   :target: https://i.imgur.com/DwZzJDo.png

Heroku_::

    heroku apps:create <nome>
    heroku run python manage.py createsuperuser
    (python console)
    from django.core.management.utils import get_random_secret_key
    get_random_secret_key()
    heroku config:set SECRET_KEY=
    heroku config:set AWS_ACCESS_KEY_ID=
    heroku config:set AWS_SECRET_ACCESS_KEY=
    heroku config:set AWS_STORAGE_BUCKET_NAME=
    heroku config:set SENTRY_DSN=
    heroku pg:backups:schedule DATABASE_URL --at '02:00 America/Sao_Paulo'

CODECOV_::

    Github > repository > secrets

Django::

    python manage.py createsuperuser
    python manage.py collectstatic
Docker::

    docker-compose up -d

DBeaver::

    Create connection with:
    Host: localhost
    Port: 5434
    Database: {{cookiecutter.project_slug}}db
    Username: {{cookiecutter.project_slug}}
    Password: see env file

Sentry_::

    Pick Django and Give your project a name

.. _AWS_IAM: https://console.aws.amazon.com/iam/home#/users$new?step=details
.. _AWS_S3: https://s3.console.aws.amazon.com/s3/bucket/create?region=sa-east-1
.. _Heroku: https://dashboard.heroku.com/apps
.. _CODECOV: https://app.codecov.io/gh/tomasrajao/{{cookiecutter.project_slug}}
.. _Sentry: https://sentry.io/organizations/tomas-0j/projects/new/