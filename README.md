# Read a csv file and use GC Notify API 

This is a simple script to read a csv file input and send emails to intended recipients using the GC Notify API (see https://notification.alpha.canada.ca).

To run:

1. Make a virtual env: `python -m venv venv`

2. Activate virtual env: `venv\Scripts\activate`

3. Install dependencies: `pip install -r requirements.txt`

4. Create env file with `template_id` and `api_key` variables.

5. Run the program: `python main.py <path to csv file for inputs>`

The input file must be a csv with three columns (based on the current template used): `email address`, `firstname`, `date`