step1 = python -m venv venv # to create environment
step2 = .\venv\Scripts\Activate.ps1 # to activate env
pip install -r requirements.txt ## to intall libraries.

to run api
uvicorn main:app --host 0.0.0.0 --port 8000
