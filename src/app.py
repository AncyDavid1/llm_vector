from fastapi import FastAPI

import os

from starlette.middleware.cors import CORSMiddleware

import routes

#PKG_NAME = os.path.dirname(os.path.realpath(__file__)).split("/")[-2]


app = FastAPI()  # -- fastapi instance -- #


def setup_app(fastapi_app: FastAPI) -> FastAPI:
    """
    setup fastapi instance with all the required configurations
    :param fastapi_app:
    :return: fastapi instance.
    """

    # -- set routers to app.
    fastapi_app.include_router(routes.llm_prediction_router)


    fastapi_app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return fastapi_app


llm_prediction = setup_app(app)