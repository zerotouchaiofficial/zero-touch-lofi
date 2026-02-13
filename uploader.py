import os
import json
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

VIDEO_FILE = "final_video.mp4"

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def upload_video():
    credentials_info = json.loads(os.environ["YOUTUBE_CREDENTIALS"])

    credentials = service_account.Credentials.from_service_account_info(
        credentials_info, scopes=SCOPES
    )

    youtube = build("youtube", "v3", credentials=credentials)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "Lofi Chill Beats 🎧 | Zero Touch AI",
                "description": "Auto generated lofi music.\n\n#lofi #chill #study",
                "tags": ["lofi", "chill", "beats"],
                "categoryId": "10"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(VIDEO_FILE, resumable=True)
    )

    response = request.execute()
    print("✅ Uploaded:", response["id"])

if __name__ == "__main__":
    upload_video()
