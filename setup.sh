#! /bin/bash
if [ ! -d 'env' ]; then # if env directory does NOT already exist then set it up
	python3 -m venv env; source env/bin/activate; python -m pip install -r requirements.txt
else # else inform user env already exists
	echo "Virtual environment already exists"
	echo "activate with 'source env/bin/activate'"
fi
