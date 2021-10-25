# Programming task for python delvelopers at IWES
## Installation
Install and update [docker](https://docs.docker.com/get-docker/) if not installed/updated already. Then follow those steps:

1. clone this repository
2. open terminal/cmd/console in the root folder
3. run `docker-compose up --build --no-start`
4. run `docker-compose up iwes-postgres-db`
5. open new terminal/cmd/console tab or window in the root folder
6. run `docker-compose run iwes-app`

The stream is ready. You are now able to paste **_single_** incoming sequences.

eg. samples from the task description:
```
$PHOCT,01,192621.400,T,00,080.378,T,-000.106,T,-03.105,T,+00.220,T,+00.084,-00.025,+00.013,+00.235,+00.024,+00.078,-0008.03*09 
$PHOCT,01,192621.500,T,00,080.311,T,-000.237,T,-03.066,T,+00.239,T,+00.105,-00.021,+00.020,+00.172,+00.042,+00.073,-0061.95*0D 
$PHOCT,01,192621.600,T,00,080.274,T,-000.329,T,-02.938,T,+00.252,T,+00.123,-00.017,+00.027,+00.205,+00.048,+00.061,+0001.33*0C 
$PHOCT,01,192621.700,T,00,080.153,T,-000.438,T,-02.926,T,+00.269,T,+00.141,-00.013,+00.032,+00.128,+00.041,+00.047,-0039.36*06
```

After stopping the application (typing in exit), the current database table ist printed. The data ist stored as long as the database service is active.

## postgreSQL database
The motion sensor information is stored as `text` in an table which is created by the python application (if the table doesn't exist).

## Usage of GPSd
I was able to match the acceptance criteria by using a postgreSQL database and a simple python application. Using GPSd seemes to add complexity where it isn't needed, yet. Maybe it will come in handy, when sensor information is processed.
