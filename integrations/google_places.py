
import requests


PLACES_URL = (
    "https://places.googleapis.com/v1/places:searchText"
)


def search_places(query, api_key, limit=10):
    if not api_key:
        raise ValueError("Google Places API key is missing.")

    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        "X-Goog-FieldMask": (
            "places.id,"
            "places.displayName,"
            "places.formattedAddress,"
            "places.location,"
            "places.rating,"
            "places.userRatingCount,"
            "places.googleMapsUri"
        )
    }

    payload = {
        "textQuery": query,
        "pageSize": min(limit, 20)
    }

    response = requests.post(
        PLACES_URL,
        headers=headers,
        json=payload,
        timeout=30
    )

    response.raise_for_status()

    data = response.json()

    return data.get("places", [])
