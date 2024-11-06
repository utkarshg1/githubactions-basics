@echo off

echo Creating python virtual environment
python -m venv venv

echo Activate venv
call venv\Scripts\activate

echo upgrade pip
python -m pip install --upgrade pip

echo install requirements.txt
pip install -r requirements.txt
