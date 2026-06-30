import os
from langchain.agents import create_agent
import sys
from pathlib import Path

project_root = str(Path(__file__).resolve().parent.parent)
if project_root not in sys.path:
    sys.path.append(project_root)


from Chunk.chunker import extract_chunks
from dotenv import load_dotenv
load_dotenv()
os.environ["GOOGLE_API_KEY"]=os.getenv("GOOGLE_API_KEY")


llm_agent=create_agent(
        model="google_genai:gemini-2.5-flash",
        tools=[]
)
# res=llm_agent.invoke({"messages":[{"role": "user", "content":"what is 123 + 456?"}]})
# print(res["messages"][-1].content)

chunks = extract_chunks("./Chunk/test_file.py")

res1=llm_agent.stream({"messages":[{"role": "user", "content":f"""here is the data:
                        
                        {chunks}
                        give me a review of one line saying whether this code is correct or not """}]})

print(res1["messages"][-1].content[0]["text"])