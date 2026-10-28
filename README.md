# dp-be

Backend for DataPilot AI: FastAPI, SQLAlchemy (async) and PostgreSQL. Scaffolding only, no features yet.

## Layout

```
app/
  main.py          app factory and lifespan (engine setup/teardown)
  api/router.py    root router, mounted under /api
  core/config.py   settings from DP_BE_* environment variables
  db/base.py       declarative Base for models
  db/session.py    engine, session factory, session dependency
tests/
```

## Run

```sh
cp .env.example .env     # fill in the passwords
make install
make db                  # Postgres on 127.0.0.1:5432
make run                 # http://localhost:8080, docs at /docs
```

Point `dp-bff` at it with `DP_BFF_UPSTREAM_URL=http://localhost:8080`. The BFF forwards `/api/...` unchanged, so routes are declared under `/api`.

## Checks

```sh
make test lint typecheck
```
