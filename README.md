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

## License
[MIT](https://choosealicense.com/licenses/mit/)
