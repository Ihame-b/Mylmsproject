from fastapi import FastAPI

from library.database.database import create_start_app_handler
from routers.auth import router


def get_application():

    # start the application.
    app = FastAPI()

    # Connect to database.
    app.add_event_handler("startup", create_start_app_handler(app))
    app.include_router(router)
    return app


app = get_application()


@app.get("/")
async def home():
    return {"detail": "hello world!"}
