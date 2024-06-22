from fastapi import FastAPI, Request
from utils.limiter import limiter, RateLimitExceeded, _rate_limit_exceeded_handler
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from routes.users import user_router


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

template = Jinja2Templates(directory = 'templates')

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# home page route
@app.get('/')
@limiter.limit('5/minute')
def home(request : Request):
    return template.TemplateResponse(
        'index.html',
        {'request': request}
    )

# users route
app.include_router(user_router)