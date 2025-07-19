
# from agents import Agent, Runner, function_tool,handoff_tool,set_tracing_disabled, OpenAIChatCompletionsModel
# from openai import AsyncOpenAI


# GEMINI_MODEL="gemini-2.0-flash"  # Specify the model you want to use, e.g., "gemini-2.0-flash"
# GEMINI_API_KEY="AIzaSyBdkgZFF2sTID6kqwOi15exkF6AXwB9S3U"
# BASE_URL="https://openrouter.ai/api/v1"


# set_tracing_disabled(disabled=True)

# client = AsyncOpenAI(
#     api_key=GEMINI_API_KEY,
#     base_url=BASE_URL,
# )

# model = OpenAIChatCompletionsModel(
#     client=client,
#     model=GEMINI_MODEL,
# )

# agent:Agent=Agent(
#     name="agent",
#     instructions="You are a helpful assistant that can answer questions and perform tasks. If you don't know the answer, " \
#     "you can ask for help or use tools to find the information.",
#     model=model

# )

# async def main():
#     result = await Runner.run(
#         agent="hello how are you?",
#         model=model,
#     )
#     print(result.final_output)

# def start():
#     import asyncio
#     asyncio.run(main())