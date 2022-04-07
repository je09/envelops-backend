from fastapi import Request, Response, status
from app.internal.utils import is_valid, vk_params_parse
from app.config import SECRET


async def valid_check(request: Request):
    return

    if request.method == "GET":
        return

    # Doesn't really work
    body = await request.json()
    if 'params' not in body:
        return status.HTTP_403_FORBIDDEN

    params = vk_params_parse(body['params'])
    valid = is_valid(query=params, secret=SECRET)
    if not valid:
        return status.HTTP_403_FORBIDDEN
