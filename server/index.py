from fastapi import FastAPI, applications

from routes.user import usersRouter
from routes.products import productsRouter
from routes.bid import BidRouter

from fastapi.middleware.cors import CORSMiddleware

# from fastapi.openapi.docs import get_swagger_ui_html


# def swagger_monkey_patch(*args, **kwargs):
#     """
#     Wrap the function which is generating the HTML for the /docs endpoint and 
#     overwrite the default values for the swagger js and css.
#     """
#     return get_swagger_ui_html(
#         *args, **kwargs,
#         swagger_js_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.29/swagger-ui-bundle.js",
#         swagger_css_url="https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.29/swagger-ui.css")


# # Actual monkey patch
# applications.get_swagger_ui_html = swagger_monkey_patch


# Your normal code ...

app = FastAPI()

origins = [
    'http://localhost:3000'
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],  
)

app.include_router(usersRouter)
app.include_router(productsRouter)
app.include_router(BidRouter)