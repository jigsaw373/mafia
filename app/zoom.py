from zoomus import ZoomClient
from flask import current_app


def get_zoom_client():
    api_key = current_app.config['ZOOM_API_KEY']
    api_secret = current_app.config['ZOOM_API_SECRET']
    api_account_id = current_app.config['ZOOM_ACCOUNT_ID']
    return ZoomClient(api_key, api_secret, api_account_id)
