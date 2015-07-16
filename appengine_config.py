import os, sys, logging
import os.path

# add `lib` subdirectory to `sys.path`, so our `main` module can load third-party libraries.
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

# set environment variable to reference client secrets google api OAuth2
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(os.path.dirname(__file__), 'client_secrets.json')
if not os.path.exists(os.environ['GOOGLE_APPLICATION_CREDENTIALS']):
    logging.error("A 'client_secrets.json', must be uploaded along with the application! Please refer to http://gspread.readthedocs.org/en/latest/oauth2.html for more information.")
