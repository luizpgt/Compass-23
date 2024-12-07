from controllers.v1Controller import handle_v1_vision 

def post_v1_vision(event, context):
    return handle_v1_vision(event)