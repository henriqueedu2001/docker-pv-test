import time
from datetime import datetime

log_file = '/logs/output.txt'

def write_log(file_path: str):
    """Writes a timestamp log on the file

    Args:
        file_path (str): the log file path
    """
    while True:
        with open(file_path, 'a') as f:
            message = f'[Log] {datetime.now()}\n'
            f.write(message)
            f.flush()
            print(message.strip())
        time.sleep(5.0)

write_log(log_file)