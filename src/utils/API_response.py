def success_response(data=None,message="Success"):
    return{
        "success":True,
        "data": data,
        "message": message
    }