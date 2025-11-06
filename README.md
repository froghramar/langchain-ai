# LangChain Sample Project

This small sample shows how to try LangChain with OpenAI locally.

What is included

- `main.py` — a tiny demo that uses LangChain's OpenAI LLM to run a simple prompt (translate to French).
- `langchain_sample/prompt_utils.py` — helper functions (pure-Python) with unit tests that don't need network.
- `tests/test_prompt_utils.py` — pytest unit test for the helper.
- `requirements.txt` — minimal dependencies to run the demo.
- `.env.example` — example environment variables file.

Quick start (Windows, bash):

1) Create a Python venv and activate it

```bash
python -m venv .venv
source .venv/Scripts/activate
```

2) Install dependencies

```bash
pip install -r requirements.txt
```

3) Configure your OpenAI API key

- Copy `.env.example` to `.env` and set `OPENAI_API_KEY` (or export it in your shell):

```bash
cp .env.example .env
# then edit .env to add your key
```

or

```bash
export OPENAI_API_KEY="sk-..."
```

4) Run the demo

```bash
python main.py
```

Notes

- If LangChain/OpenAI packages are not installed or your API key is missing, `main.py` will print guidance.
- The tests are pure-Python and do not call the network. Run them with `pytest -q`.

Next steps

- If you want an example that doesn't rely on OpenAI, I can add a local mock LLM or a sample that uses a local model provider.
