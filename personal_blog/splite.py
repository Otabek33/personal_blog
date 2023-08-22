import os

from split_settings.tools import include

# Include the base settings file
include('base.py')

# Include the environment-specific settings file based on the environment
if 'production' in os.environ.get('DJANGO_SETTINGS_MODULE', ''):
    include('production.py')
elif 'local' in os.environ.get('DJANGO_SETTINGS_MODULE', ''):
    include('local.py')
