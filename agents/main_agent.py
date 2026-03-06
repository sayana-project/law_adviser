from openai import OpenAI
import os
from dotenv import load_dotenv
import yaml
load_dotenv()
#APIKEY=os.getenv('OPENROUTER_APIKEY')

class Agents():

    def __init__(self):
        self.apikey = os.getenv('OPENROUTER_APIKEY')
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=self.apikey
        )
        with open("agents/prompts/main_agent.yaml", "r") as f:
            config = yaml.safe_load(f)
        self.system_prompt = config["system_prompt"]

    def llm_output(self,prompt):

        completion = self.client.chat.completions.create(
            extra_body={},
            model=os.getenv('MODEL'),
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                    }
                ] + prompt
        )
        return completion.choices[0].message.content
        