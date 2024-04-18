from routes.routers.router import llm_prediction_router


@llm_prediction_router.post("/")
async def create_product_query():

    return {"say":"helllo"}

