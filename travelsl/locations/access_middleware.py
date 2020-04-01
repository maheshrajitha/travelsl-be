import json
from functools import wraps
def check_role(role):
    def executer(view):
        @wraps(view)
        def wrapper_middleware(request):
            request_body = json.loads(request.body)
            if request_body.get("role") == role:
                return view(request)
            else:
                raise Exception("UNAUTHORIZED")
        return wrapper_middleware
    return executer
