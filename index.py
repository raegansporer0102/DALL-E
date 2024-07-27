# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json

client = AzureOpenAI(
    api_version="2024-02-01",
    azure_endpoint="https://rajat-gpt.openai.azure.com/",
    api_key=os.environ["b2a2a1bdb9524e22af82eec6036221d4"],
)

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="<the user's prompt>",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
