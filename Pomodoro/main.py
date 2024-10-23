from handlers import routers
from fastapi import FastAPI

app = FastAPI()

for router in routers:
    app.include_router(router=router)


