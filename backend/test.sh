source venv/bin/activate
export SECRET_KEY=b'_5#y2L"F4Q8z\n\xec]/'
export UPLOAD_FOLDER=static/uploaded/
export DATABASE_URI=postgresql://jjoc:1234@localhost:5432/modacheap_v2_test
export FLASK_APP=server
export FLASK_ENV=development
python3 -m unittest "tests/test_app.py"