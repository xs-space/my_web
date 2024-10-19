from fastapi import FastAPI

from apis.routers import router


def create_app():
    app = FastAPI(
        debug=True,
        version='1.0.1',
        title='个人网站',
        description='我的个人网站'
    )

    app.include_router(router)
    return app
