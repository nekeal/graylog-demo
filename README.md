# Graylog-demo

Demo python which presents logging to graylog

## Installation

    docker-compose pull
    docker-compose build

## Usage

Run all services 
    
    docker-compose up
    
Go to http://localhost:9000 and login with admin:admin credentials.
Create `GELF UDP` input on address `0.0.0.0` and port `12201`. Other
options leave as default.

Now you should see your logs [here](http://localhost:9000/search)

## Logging best practices

GELF stands for Graylog Extended Log Format and is used for structured logging and 
storing logs in graylog. 
There are some factors which should be taken into account when setting up loggers in
application.

### Logging levels

There are couple logging levels and each should be used in particular case:

* DEBUG - for debugging purposes (mostly in development(. Usually contains a lot of context
* INFO - use it when something important and expected happens (e.g. new scrapping job is started)
* WARNING - indicates that something unusual or unexpected happens but it's not an error
* ERROR - it is used to indicate that some error happened but it can be handled (e.g. internal exceptions, errors from API) 
* CRITICAL - application is in unrecoverable state and an manual action should e taken 


### Log timestamp

Each log entry should have timestamp included. 
It is automatically handled by `BaseGELFHandler` from graypy package.

### Log context

To easily find place in code where log entry was created it is necessary to include that information
in entry. Initializing `BaseGELFHandler` with `debugging_fields=True` (default) extends log entry
by: file name, function name, line number, thread name and even pid.

In some cases it is required to include some context variables. By default 
`BaseGELFHandler` adds information from `extra` dict passed to logger.

```python
   logger.info("Scrapping has started", extra={"job_id": job_id})
```

### Logging host 

By default source name is determined by hostname so it is important to
specify it manually because docker chooses it randomly.

Docker compose example:

```yaml
version: '3'

services:
  scrapper:
    hostname: scrapper-reddit
    build: .
```

## License
[MIT](https://choosealicense.com/licenses/mit/)
