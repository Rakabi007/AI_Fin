#!/usr/bin/env python
from ai_fin_latest.crew import AiFinLatestCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {
        'topic': 'AI LLMs'
    }
    AiFinLatestCrew().crew().kickoff(inputs=inputs)