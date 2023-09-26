# Alembic

## Sync

```bash
alembic init migrations
```

## Async

```bash
alembic init -t async migrations
```

Configure necessary files.

```bash
alembic revision --autogenerate -m "initial migration"
```

```bash
alembic upgrade head
```
