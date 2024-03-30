# weather-app

## Commands

- Run the project:

```bash
docker-compose up --force-recreate --build --remove-orphans -d
```

- access the database:

```bash
mysql -u root -p
```

- query the database:

```sql
use weather_app;
select * from cache;
```
