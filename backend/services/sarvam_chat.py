import os

from dotenv import load_dotenv
from sarvamai import SarvamAI

load_dotenv()

API_KEY = os.getenv("SARVAM_API_KEY")

client = SarvamAI(
    api_subscription_key=API_KEY
)


def generate_response(prompt: str):

    response = client.chat.completions(
        model="sarvam-105b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content