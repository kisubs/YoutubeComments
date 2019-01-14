import flask
from flask import make_response, abort, session, Blueprint, request
import google.oauth2.credentials
#import google_auth_oauthlib.flow
import googleapiclient.discovery

video = Blueprint('video', __name__)

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account and requires requests to use an SSL connection.
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl', 'https://www.googleapis.com/auth/userinfo.profile', 'https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/plus.me']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'

@video.route('/video')
def home():
    videoId = request.args.get('v', type = str)
    # Load the credentials from the session.
    credentials = google.oauth2.credentials.Credentials(
        **flask.session['credentials'])

    client = googleapiclient.discovery.build(
        API_SERVICE_NAME, API_VERSION, credentials=credentials)
    return comment_threads_list_by_video_id(client,
            part='snippet,replies',
            videoId=videoId)
    #return videoId
# Remove keyword arguments that are not set
def remove_empty_kwargs(**kwargs):
    good_kwargs = {}
    if kwargs is not None:
        for key, value in kwargs.items():
            if value:
                good_kwargs[key] = value
    return good_kwargs

def comment_threads_list_by_video_id(client, **kwargs):
    # See full sample for function
    kwargs = remove_empty_kwargs(**kwargs)

    response = client.commentThreads().list(
        **kwargs
    ).execute()

    return flask.jsonify(**response)
