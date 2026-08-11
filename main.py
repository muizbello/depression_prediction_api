# import logging
from fastapi import FastAPI,Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from schemas.student import Student


app = FastAPI()

limiter = Limiter(key_func=get_remote_address)

app.state.limiter = limiter
app.add_exception_handler(
    RateLimitExceeded,
    _rate_limit_exceeded_handler
)

# logging.basicConfig(
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )

# logger = logging.getLogger(__name__)

@app.get("/")
async def home():
    return {"message": "hello"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.get("/about")
async def about():
    return {"response": "This API allows you to access ML models for student depression prediction"}


@app.post("/predict")
@limiter.limit("10/minute")
async def predict_depression(student: Student):
    return {"Age:": student.age,
            "Program of Study": student.program
    }
