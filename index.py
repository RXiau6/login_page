from fastapi import FastAPI
from routes.index  import user
from config.db import meta, engine
app = FastAPI()

app.include_router(user)
meta.create_all(engine)