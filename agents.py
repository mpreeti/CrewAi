from crewai import Agent,LLM
from tools import tool
from dotenv import load_dotenv
load_dotenv()
from langchain_google_genai import ChatGoogleGenerativeAI
import os
from langchain_huggingface import HuggingFaceEndpoint

# repo_id = "mistralai/Mistral-7B-Instruct-v0.2"

# llm = HuggingFaceEndpoint(
#     repo_id=repo_id,
#     # max_length=128,
#     temperature=0.5,
#     huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
# )
# from litellm import completion
# llm = completion(
#     model="gemini/gemini-pro",
#     GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY"),
#     temperature=0.5,  # Optional
#     verbose=True      # Optional
# )

# ## call the gemini models
# llm=ChatGoogleGenerativeAI(model="gemini-1.5-pro",
#                            verbose=True,
#                            temperature=0.5,
#                            google_api_key=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
# )



# Creating a senior researcher agent with memory and verbose mode
ollama_llm= LLM(
    model='ollama/llama3.2:1b',
    base_url='http://localhost:11434/'
)

news_researcher=Agent(
    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."

    ),
    tools=[tool],
    llm=ollama_llm,
    allow_delegation=True

)

## creating a write agent with custom tools responsible in writing news blog

news_writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[tool],
  llm=ollama_llm,
  allow_delegation=False
)
