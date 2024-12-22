from crewai import Agent
from tools import tool
from dotenv import load_dotenv
import os
from langchain_huggingface import HuggingFaceEndpoint
from litellm import completion
# Load environment variables
load_dotenv()

# # Define Hugging Face LLM
# llm = HuggingFaceEndpoint(
#     endpoint_url="https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2",
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
#     temperature=0.5
# )

llm = completion(
    model= "gemini/gemini-pro",
    GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY"),
    temperature=0.5,
    verbose=True
)

# Senior Researcher Agent
news_researcher = Agent(
    role="Senior Researcher",
    goal="Uncover ground-breaking technologies in {topic}",
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        " innovation, eager to explore and share knowledge that could change"
        " the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

# Test LLM
try:
    response = llm.call("Explain the next big trend in AI healthcare.")
    print("LLM Response:", response)
except Exception as e:
    print("Error during LLM call:", e)
