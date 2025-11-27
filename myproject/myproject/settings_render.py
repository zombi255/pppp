import dj_database_url

DATABASES = {
    'default': dj_database_url.parse(
        "postgresql://demodb_8fyj_user:QgWOL4zv9iydMgSlgjl6heRkXXkhjNwc@dpg-d4k84fruibrs73fatrsg-a.oregon-postgres.render.com/demodb_8fyj"
    )
}
