# weather-app

## prepare the environment

- create a `.env` file in the root of the project with the following content:

```bash
DB_HOST=db
DB_PORT=3306
DB_USER=root
DB_PASSWORD=password
DB_NAME=weather_app
APP_PORT=3000
WEATHER_API_KEY=your_api_key
```

you can get an api key from [openweathermap](https://home.openweathermap.org/users/sign_up)
also will will have a file named `.env.example` with the same content you can copy it and rename it to `.env`

## Commands to run the project

- Run the project:

```bash
docker-compose up --force-recreate --build --remove-orphans -d
```

- access the database:

in the mysql container terminal run:

```bash
mysql -u root -p
```

- query the database:

```sql
use weather_app;
select * from cache;
```

- run pytest tests:

to run the tests you can use the following command:

```bash
docker-compose run app pytest .
```

- make a request to the api:

to make a request to the api you can use the following command:

```bash
curl -v -L "http://localhost:8000/weather?city=cairo&country=eg"
```

or you can access to the swagger documentation by visiting:

[swagger](http://localhost:8000/docs)

or the redoc documentation by visiting:

[swagger](http://localhost:8000/redoc)
