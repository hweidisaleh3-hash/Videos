
import requests


BASE_URL = "https://api.minimax.io"
MODEL = "MiniMax-H3"


def create_video_task(
    prompt,
    api_key,
    duration=4,
    resolution="768P",
    ratio="16:9"
):
    """Create an H3 video generation task."""

    if not api_key:
        raise ValueError("MiniMax API key is required.")

    if not prompt or not prompt.strip():
        raise ValueError("Video prompt cannot be empty.")

    if duration < 4 or duration > 15:
        raise ValueError("Duration must be between 4 and 15 seconds.")

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": MODEL,
        "content": [
            {
                "type": "text",
                "text": prompt
            }
        ],
        "duration": duration,
        "resolution": resolution,
        "ratio": ratio
    }

    response = requests.post(
        f"{BASE_URL}/v2/video_generation",
        headers=headers,
        json=payload,
        timeout=120
    )

    response.raise_for_status()
    return response.json()


def get_video_status(task_id, api_key):
    """Check the status of an H3 video task."""

    headers = {
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.get(
        f"{BASE_URL}/v2/query/video_generation/{task_id}",
        headers=headers,
        timeout=30
    )

    response.raise_for_status()
    return response.json()
