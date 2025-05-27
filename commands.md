initialize alembic
```bash
alembic init -t async alembic
```

create migration (in project directory with alembic.ini)
```bash
alembic revision --autogenerate -m "migration_name"
```

do migration
```bash
alembic upgrade head
```

downgrade to prev migration
```bash
alembic downgrade -1
```