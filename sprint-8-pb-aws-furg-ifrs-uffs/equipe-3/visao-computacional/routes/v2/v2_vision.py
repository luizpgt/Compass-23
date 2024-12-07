from controllers.v2Controller import handle_v2_vision 

def post_v2_vision(event, context):
    return handle_v2_vision(event)