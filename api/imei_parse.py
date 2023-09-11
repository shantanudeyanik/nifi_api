import json

def imei_data(input_data):
    input_data = input_data
    data = json.loads(input_data)

    output_data = []

    for i, user_data in enumerate(data["f_req_fcm_data"]):
        user_id = user_data["user_id"]
        result_item = data["f_rsp_text"]["results"][i]

        if "message_id" in result_item:
            result = "message"
        elif "error" in result_item:
            result = "error"
        else:
            result = "unknown"  # Handle other cases as needed

        output_item = {
            "imei": data["imei"],
            "user_id": user_id,
            "result": result
        }

        output_data.append(output_item)
    return output_data
