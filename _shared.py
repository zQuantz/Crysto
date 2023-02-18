from pathlib import Path
import logging
import os
DIR = Path(os.path.realpath(os.path.dirname(__file__)))
DATA_DIR = DIR / "data"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'{DIR}/log.log')
formatter = logging.Formatter('%(asctime)s - %(message)s')
fh.setLevel(logging.DEBUG)
fh.setFormatter(formatter)
logger.addHandler(fh)