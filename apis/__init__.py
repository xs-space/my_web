from fastapi import FastAPI


def create_app():
    app = FastAPI(
        debug=True,
        version='1.0.1',
        title='个人网站',
        description='我的个人网站'
    )
    return app