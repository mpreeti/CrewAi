from crewai import Crew,Process,LLM
from tasks import research_task, write_task
from agents import news_researcher,news_writer

## Forming the tech focused crew with some enhanced configuration
crew=Crew(
    agents=[news_researcher,news_writer],
    tasks=[research_task,write_task],
    process=Process.sequential,

)

ollama_llm= LLM(
    model='ollama/llama3.2:1b',
    base_url='http://localhost:11434/'
)
## starting the task execution process wiht enhanced feedback

result=crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)