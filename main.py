"""Tiny LangChain demo.

This script will attempt to use LangChain + OpenAI if installed and if
`OPENAI_API_KEY` is present in the environment. If those aren't set,
it prints guidance so you can install and configure the project.
"""

from dotenv import load_dotenv
import os

load_dotenv()

def run_demo(text: str = "Hello, how are you?") -> str:
    """Run a tiny LangChain demo that asks the model to translate to French.

    Raises RuntimeError if OPENAI_API_KEY is not present.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. See README.md to configure it.")

    # Import LangChain lazily so the module can be inspected even if not installed
    try:
        from langchain.llms import OpenAI
        from langchain.prompts import PromptTemplate
        from langchain.chains import LLMChain
    except Exception as e:
        raise RuntimeError("LangChain or required components are not installed: " + str(e))

    llm = OpenAI(temperature=0)
    prompt = PromptTemplate(input_variables=["text"], template="Translate to French: {text}")
    chain = LLMChain(llm=llm, prompt=prompt)
    result = chain.run(text)
    return result


if __name__ == "__main__":
    try:
        out = run_demo()
        print("Demo output:\n", out)
    except Exception as err:
        print("Could not run the demo:", err)
        print("See README.md for setup instructions (venv, requirements, .env).")
