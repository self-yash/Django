from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

#Write your Middleware Classes here-
class CustomHeaderMiddleware(MiddlewareMixin):
    def process_response(self, request, response):
        response["X-Powered-By"] = "Fester's Django App"
        response["X-App-Version"] = "1.0.0"

        return response
    

class SimpleAuthMiddleware(MiddlewareMixin):
    VALID_API_KEY = "fester"

    def process_request(self, request):
        api_key = request.headers.get("X-API-KEY")
        if api_key != self.VALID_API_KEY:
            return JsonResponse({"msg": "Unauthorized"}, status=401)
        # If valid, request proceeds to the view

class RoleValidationMiddleware(MiddlewareMixin):
    ROLE_MAP={
        "/api/students/create/": ["admin"],
        "/api/students/list/": ["admin"],
        "/api/students/view/": ["admin", "student"],
        "/api/students/update/": ["admin", "student"],
        "/api/students/delete/": ["admin"],
    }

    def process_request(self,request):
        for path_prefix,allowed_roles in self.ROLE_MAP.items():
            if request.path.startswith(path_prefix):
                role=request.headers.get("X-user-role")
                if role not in allowed_roles:
                    return JsonResponse({"msg":f"Access denied to role {role}"},status=403)
        # path=request.path
        # role=request.headers.get("X-user-role",None)

        # if path not in self.ROLE_MAP:
        #     return None
        
        # allowed_rol
