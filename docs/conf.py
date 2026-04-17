import os
import sys

sys.path.insert(0, os.path.abspath('.'))

# Project information
project = 'HR Block Fast Track'
author = 'Elemor'
release = '1.0'

# General configuration
extensions = [
    "sphinx_rtd_theme",
]

templates_path = ['_templates']
exclude_patterns = []

# HTML output
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

# Google site verification (FIXED)
html_meta = {
    "google-site-verification": "xMvhEb7ayr2oSB67CmQJ-XqQ7Pati-Stu9KHRdN-J6c"
}
