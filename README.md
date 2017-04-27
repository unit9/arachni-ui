# Arachni UI
This is a very simple web ui for [Arachni](http://www.arachni-scanner.com)
security scanner which runs the cli version of the scanner using
[Celery](http://www.celeryproject.org) for running the background tasks and
[Redis](https://redis.io) for storing the results.

You need to provide the following environment variables:

- `DEBUG` - either 0 or 1, optional, set to 0
- `SCANNER_PATH` - absolute path to arachni scanner, e.g. `/bin/arachni`
- `SCANNER_REPORT_PATH` - path to a dir where to save reports
- `CC_EMAIL` - email address to send report to
- `BCC_EMAIL` - email address to send report to
- `FROM_EMAIL` - sender's email
- `SMTP_SERVER` - smtp server's address
- `SMTP_PORT` - smtp server's port, optional, set to 25
- `SMTP_USERNAME` - server's login, optional
- `SMTP_PASSWORD` - server's password, optional
- `CELERY_BROKER_URL` - [broker url](http://docs.celeryproject.org/en/latest/getting-started/brokers/index.html) for Celery
- `CELERY_RESULT_BACKEND` - [result backend](http://docs.celeryproject.org/en/latest/userguide/configuration.html#std:setting-result_backend) to store scan results
