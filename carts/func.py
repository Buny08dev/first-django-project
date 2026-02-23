from carts.models import CartsModel

def get_users_carts(request):
    if request.user.is_authenticated:
        return CartsModel.objects.filter(user=request.user)
    else:
        if request.session.session_key:
            return CartsModel.objects.filter(session_key=request.session.session_key)
        else:
            request.session.create()
            return CartsModel.objects.filter(session_key=request.session.session_key)