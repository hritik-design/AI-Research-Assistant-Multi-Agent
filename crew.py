from crewai import Crew

from agents.research_specialist import research_specialist_agent
from agents.data_analyst import data_analyst_agent
from agents.content_writer import content_writer_agent
from tasks.research_task import create_research_task
from tasks.analysis_task import create_analysis_task
from tasks.writing_task import create_writing_task

def get_research_crew():
    rt = create_research_task()
    at = create_analysis_task(rt)
    wt = create_writing_task(rt, at)
    
    return Crew(
        agents=[
            research_specialist_agent,
            data_analyst_agent,
            content_writer_agent,
        ],
        tasks=[
            rt,
            at,
            wt,
        ],
        verbose=True,
        max_rpm=30,
        cache=False
    )