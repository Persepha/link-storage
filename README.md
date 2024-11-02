
# Тестовое задание

Тестовое задание на позицию Junior Python Developer**   


## Run Locally

Clone the project

```bash
  git clone https://github.com/Persepha/link-storage.git
```

Go to the project directory

```bash
  cd link-storage
```

Run the docker containers:

```bash
  make build-server
```

or 

```bash
  docker-compose up --build
```


Test it out at http://localhost:8000. 


## Documentation

Swagger docs at 

http://localhost:8000/api/schema/swagger-ui/

Default superuser for admin panel

email
```bash
    admin@test.com
```

login
```bash
    admin
```

pass
```bash
    admin123
```

For generate fake data for database use command 

```bash
make seed-data
```

or use command 
```bash
docker-compose exec web /opt/venv/bin/python manage.py  seed_data NUMBER_USER NUMBER_LINK
```
example
```bash
docker-compose exec web /opt/venv/bin/python manage.py  seed_data 10 300
```


Task part 2 SQL query in file "tasks2_count_links"

or

```sql
SELECT auth_user.email, 
       ranked_links.count_links,
       ranked_links.website,
       ranked_links.book,
       ranked_links.article,
       ranked_links.music,
       ranked_links.video
FROM auth_user
JOIN (
    SELECT user_id, 
           COUNT(*) AS count_links,
           COUNT(*) FILTER (WHERE link_type = 'website') AS website,
           COUNT(*) FILTER (WHERE link_type = 'book') AS book,
           COUNT(*) FILTER (WHERE link_type = 'article') AS article,
           COUNT(*) FILTER (WHERE link_type = 'music') AS music,
           COUNT(*) FILTER (WHERE link_type = 'video') AS video
    FROM storage_link
    GROUP BY user_id
) AS ranked_links ON auth_user.id = ranked_links.user_id
ORDER BY ranked_links.count_links DESC, auth_user.date_joined ASC
LIMIT 10;
```


## notes

- Email token for reset password sends into console
- For creating link_collection using swagger add link_ids through , (for example "1, 4, 7")






