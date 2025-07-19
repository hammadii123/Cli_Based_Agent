import asyncio
import os
from dotenv import load_dotenv

from agents import Agent, RunConfig, Runner
# from agents.models import OpenAIChatCompletionsModel 
from agents.models.openai_chatcompletions import OpenAIChatCompletionsModel


from openai import AsyncOpenAI




load_dotenv()



GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("GEMINI_API_KEY not found in environment variables. Please ensure it's set in your .env file.")


GEMINI_MODEL: str = "gemini-2.0-flash"


BASE_URL: str = "https://generativelanguage.googleapis.com/v1beta/openai/"


client: AsyncOpenAI = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)


model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(model=GEMINI_MODEL, openai_client=client)


text_generator_agent: Agent = Agent(
    name="Text Generator",
    instructions="You are a helpful assistant that answers questions directly and concisely.",
    model=model,
)

async def main():
    """
    Main asynchronous function jo Gemini query ko agents library ke through run karegi.
    """
    print("Application is preparing to send query using Agents library...")
    

    query = "Is Pakistan better than America?"
    
    print(f"Sending query to Gemini using model '{GEMINI_MODEL}': '{query}'")
    
    
 
    result = await Runner.run(text_generator_agent, query, run_config=RunConfig(model=model))
    
    print("Received response from Gemini.")
    print("\n--- Final Output ---")
    
 
    print(result.final_output)

def start():
    """
    Synchronous entry point jo asynchronous main function ko run karti hai.
    """
    print("Starting the application...")
    asyncio.run(main()) 
    print("Application finished.")


if __name__ == "__main__":
    start()

