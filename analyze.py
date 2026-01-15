import json
import os
from typing import Any, Dict
from dotenv import load_dotenv
from litellm import completion

# You can replace these with other models as needed but this is the one we suggest for this lab.
MODEL = "groq/llama-3.3-70b-versatile"
load_dotenv()

# api_key = os.environ.get("LITELLM_API_KEY")


def get_itinerary(destination: str) -> Dict[str, Any]:
    """
    Returns a JSON-like dict with keys:
      - destination
      - price_range
      - ideal_visit_times
      - top_attractions
    """
    # implement litellm call here to generate a structured travel itinerary for the given destination

    # See https://docs.litellm.ai/docs/ for reference.

    data = completion(
        model=MODEL,
        messages=[
                {
                    "role": "system",
                    # CRITICAL: Llama 3 requires explicit instruction to use JSON
                    "content": "You are a helpful assistant. You must respond with valid JSON only. Do not add any markdown formatting like ```json ... ```."
                },
                {
                    "role": "user",
                    "content": f"Extract a structured travel itinerary details from this text into JSON format, the JSON should only include destination, price_range, ideal_visit_times, and top_attractions: {destination}"
                }
            ],
            # 3. Enable JSON mode
            response_format={"type": "json_object"}, 
            temperature=0.1
    )    

    content_str = data.choices[0].message.content

    # 2. Parse the string into a Python Dictionary
    # Since you requested JSON mode, this string is valid JSON.
    data = json.loads(content_str)

    return data
