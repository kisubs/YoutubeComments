from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

# Data to serve with our API
COMMENTS = {
    1: {
        "id": 1,
        "comment": "sfu is trash",
        "timestamp": get_timestamp()
    },
    2: {
        "id": 2,
        "comment": "yolo",
        "timestamp": get_timestamp()
    },
    3: {
        "id": 3,
        "comment": "fml",
        "timestamp": get_timestamp()
    },
    4: {
        "id": 4,
        "comment": "raincouver",
        "timestamp": get_timestamp()
    },
    5: {
        "id": 5,
        "comment": "youtube",
        "timestamp": get_timestamp()
    }
}

# Create a handler for our read (GET) people
def read():
    """
    This function responds to a request for /api/people
    with the complete lists of people

    :return:        sorted list of people
    """
    # Create the list of people from our data
    return [COMMENTS[key] for key in sorted(COMMENTS.keys())]
