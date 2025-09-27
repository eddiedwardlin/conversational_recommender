# conversational_recommender

Conversational recommder comparison study.

### Instructions
1. Install Ollama (https://ollama.com)
2. Run `ollama pull gpt-oss:20b` to install gpt-oss:20b model
3. Create and activate virtual environment
    - Run `python3 -m venv env` 
    - Run `source env/bin/activate`
4. Install dependencies
    - Run `pip install -r requirements.txt`
5. Run conversational recommender scripts
    - Run `python3 direct.py` to run direct recommender
    - Run `python3 structured.py` to run structured recommender
6. Responses appear in `/responses` or `/rag_responses` respectively
7. Add data files to `./data` if needed