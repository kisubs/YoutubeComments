from flask import make_response, abort, session, Blueprint, request

video = Blueprint('video', __name__)
@video.route('/video')
def home():
    videoId = request.args.get('v', type = str)

    return videoId
