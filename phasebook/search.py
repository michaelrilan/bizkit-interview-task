from flask import Blueprint, request,jsonify

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return jsonify(search_users(request.args.to_dict())), 200

def is_substring(input_string, data_string):
    # Check if input_string is a substring of data_string
    if input_string.lower() in data_string.lower():
        return True
    else:
        return False
    

def search_users(args):
    filtered_users = []
    
    for user in USERS:
        
        age = int(args["age"]) if "age" in args else None
         # If id is the only parameter
        if "id" in args and "name" not in args and "age" not in args and "occupation" not in args:
            if user["id"] == args["id"]:
                filtered_users.append(user)

         # If the id and name is the only parameter
        elif "id" in args and "name" in args and "age" not in args and "occupation" not in args:
            # Check name parameter (case-insensitive partial match)
            if user["id"] == args["id"] or args["name"].lower() in user["name"].lower():
                filtered_users.append(user)


        # If the age is the only parameter
        elif "id" not in args and "name" not in args and "age" in args and "occupation" not in args:
            
            if int(user["age"]) <= age + 1 and int(user["age"]) >= age - 1:
                filtered_users.append(user)

        # If all datas are inside the parameter
        elif "id" in args and "name" in args and "age" in args and "occupation" in args:

            if user["id"] == args["id"] or args["name"].lower() in user["name"].lower() or is_substring(args["occupation"],user["occupation"]) or (int(user["age"]) <= age + 1 and int(user["age"]) >= age - 1):
                filtered_users.append(user)
    return filtered_users

