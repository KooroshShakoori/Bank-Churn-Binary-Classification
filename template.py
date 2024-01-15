import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]:  %(message)s')

project_name = 'Bank Churn Prediction'

file_list = [
    'github/workflows/.gitkeep',
    f'src/{project_name}/__init__.py',
    f'src/{project_name}/components/__init__.py',
    f'src/{project_name}/utils/__init__.py',
    f'src/{project_name}/config/__init__.py',
    f'src/{project_name}/config/configuration.py',
    f'src/{project_name}/pipeline/__init__.py',
    f'src/{project_name}/entity/__init__.py',
    f'src/{project_name}/constants/__init__.py',
    'config/config.yaml',
    'dvc.yaml',
    'params.yaml',
    'requirements.txt',
    'setup.py',
    'research/trials.ipynb',
    'templates/index.html'
]

for file in file_list:
    filepath = Path(file)
    filedir, filename = filepath.parent, filepath.name
    if filedir != '':
        os.makedirs(filedir, exist_ok=True)

        logging.info(f'created directory: {filedir} for file: {filename}')

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass

        logging.info(f'created file: {filepath}')

    else:
        logging.info(f'file: {filepath} already exists, skipping ...')