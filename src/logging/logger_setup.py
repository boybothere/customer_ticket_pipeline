import os
import logging
from datetime import datetime

LOG_FOLDER=os.path.join("logs",datetime.now().strftime('%d_%m_%Y_%H_%M_%S_%f'))
os.makedirs(LOG_FOLDER, exist_ok=True)

LOG_FILE=os.path.splitext(os.path.basename(__file__))[0]

logging.basicConfig(
    filename=os.path.join(LOG_FOLDER, f"app.log"),
    format="%(asctime)s - %(lineno)d %(name)s %(levelname)s -> %(message)s",
    level=logging.INFO
)

