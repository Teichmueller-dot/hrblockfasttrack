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
    "msvalidate.01": "15C4041BD69D3D2E2994470D5BF8A9C4"
}
