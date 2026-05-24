from openai import OpenAI
from dotenv import load_dotenv
import os
load_dotenv()
client = OpenAI(
  api_key=os.getenv("NVIDIA_API_KEY"),
  base_url="https://integrate.api.nvidia.com/v1"
)

response = client.embeddings.create(
    input=["What is the capital of France?"],
    model="nvidia/llama-nemotron-embed-1b-v2",
    encoding_format="float",
    extra_body={"input_type": "query", "truncate": "NONE"}
)

print(response.data[0].embedding)

