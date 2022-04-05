from fastapi import APIRouter, Depends
from app.internal.group import schemas
from app.internal.group import crud
from app.dependencies import get_db
from app.internal.utils import is_valid

from urllib.parse import urlparse, parse_qsl, urlencode

router = APIRouter()


@router.post("/")
def create_user(group: schemas.Group, db=Depends(get_db)):
    # return crud.create_group(db, group)
    u = 'example.com/' + group.params
    client_secret = 'h6Udtkw8FTCFTzxcms24'
    query_params = dict(parse_qsl(urlparse(u).query, keep_blank_values=True))
    status = is_valid(query=query_params, secret=client_secret)
    return {
        "result": "ok",
        "error": "",
    }