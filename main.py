import logging
from urllib.parse import urlparse
import os
import json
import datetime as dt

# import fastapi service modules
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse

# import starlette service modules
from starlette.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware import Middleware
from router import router

fastapi_app = FastAPI()
fastapi_app.mount("/static", StaticFiles(directory="static"), name="static")
fastapi_app.include_router(router)