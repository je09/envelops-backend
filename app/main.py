from fastapi import Depends, FastAPI, Request, status, Response
from fastapi.middleware.cors import CORSMiddleware
from app.routes import group, user, scenario
from app.middleware import valid_check
from app.database import create_tables, SessionLocal

app = FastAPI()
create_tables()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/", status_code=status.HTTP_200_OK)
def index():
    return {"result": "ok"}


app.include_router(group.router, prefix="/groups", tags=["groups"], dependencies=[Depends(valid_check)])
app.include_router(user.router, prefix="/users", tags=["users"], dependencies=[Depends(valid_check)])
app.include_router(scenario.router, prefix="/scenarios", tags=["scenarios"], dependencies=[Depends(valid_check)])
