"""
A wrapper script to run the Pelican website gen on Windows.

This script was created in response to a bug on some Windows systems,
where the user wasn't able to kill the Pelican gen process with Ctrl+C.
Issue: https://github.com/techartorg/techartorg.github.io/issues/2

This script tries to kill the process with Ctrl+C. If this doesn't kill the
Pelican process we call `.kill()` on the Pelican proc object.
"""

import os
import logging
import signal
import subprocess
import sys
import time


class RunPelican:
    """
    Wrapper for running Pelican hot reload
    """

    def __init__(self, python_exe_path):
        """
        Init Pelican runner
        """
        self.pelican_proc = None
        self.python_exe_path = python_exe_path

    def __proc_ctrl_c(self, *_):
        """
        Attempt to stop the Pelican process
        """
        logging.info('Press Ctrl+C')

        if self.pelican_proc:
            attempts = 3
            while self.pelican_proc.poll() is None and attempts:
                time.sleep(1)
                logging.debug(f'Sending CTRL_C_EVENT to PID {self.pelican_proc.pid}')
                os.kill(self.pelican_proc.pid, signal.CTRL_C_EVENT)
                attempts -= 1

            if self.pelican_proc.poll() is None:
                logging.debug(f'Killing process with PID {self.pelican_proc.pid}')
                self.pelican_proc.kill()

            sys.exit(0)
        else:
            logging.warning("The Pelican process is not running."
                            "Can't stop a process that isn't running.")

    def run_pelican_hot_reload(self):
        """
        Start the Pelican site gen and hot reload process
        """
        cmd = [self.python_exe_path, '-m', 'pelican',
               '--debug', '-lr', 'content', '-o', 'output', '-s', 'pelicanconf.py']
        logging.info('start dev server:\n' + " ".join(cmd))

        self.pelican_proc = subprocess.Popen(cmd, shell=True)

        signal.signal(signal.SIGINT, self.__proc_ctrl_c)

        while True:
            pass


def select_python_venv(py_venvs, tox_dir):
    """
    Get user input to select one of the available
    Python venv(s)
    """
    logging.info('There are more than one amiable Python venv(s) in the .tox dir.')
    while True:
        print(f"\n\nPick one of the available python venv(s) in '{tox_dir}'.")
        for i, penv in enumerate(py_venvs):
            print(i, penv)

        index = input('Enter the index of the python venv you want: ')
        try:
            py_venv = py_venvs[int(index)]
            return py_venv
        except Exception as exc:
            print('\nException:\n', str(exc))
            print(f'error: {index} is not a valid index. Please try again...')


def find_python_venv():
    """
    Make sure that the Python virtual env was installed,
    and return the path to the python.exe.

    If there are multiple python exe(s) then ask what venv does the user want to use.
    """
    install_instructions = "You can find instructions on how to setup your workspace here: " \
                           "https://github.com/techartorg/techartorg.github.io"

    tox_dir = os.path.join(os.path.dirname(__file__), '.tox')
    if not os.path.isdir(tox_dir):
        logging.error(f"Didn't find {tox_dir}.\nMake sure you run the tox setup.")
        logging.info(install_instructions)
        sys.exit(-1)

    logging.info(f"Using tox folder located here: {tox_dir}")

    py_venvs = [folder for folder in os.listdir(tox_dir) if 'py' in folder]

    if not py_venvs:
        logging.error(f"Didn't find any python venv(s) in '{tox_dir}'.\n"
                      "Make sure you run the tox setup.")
        logging.info(install_instructions)
        sys.exit(-1)

    if len(py_venvs) == 1:
        py_venv = py_venvs[0]
    else:
        py_venv = select_python_venv(py_venvs, tox_dir)

    python_exe = os.path.join(tox_dir, py_venv, 'Scripts', 'python.exe')

    if not os.path.isfile(python_exe):
        logging.error(f"Didn't find a python exe located at '{python_exe}'.\n"
                      "Make sure you run the tox setup.")
        logging.info(install_instructions)
        sys.exit(-1)

    logging.info(f"Using Python located here: {python_exe}")
    return python_exe


def main():
    """
    The main func of WinPelicanRunner
    """
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger("WinPelicanRunner")

    if os.name != 'nt':
        log.error("This script was made to run on windows!")
        sys.exit(-1)

    python_exe_path = find_python_venv()

    pel_run = RunPelican(python_exe_path)
    pel_run.run_pelican_hot_reload()


if __name__ == "__main__":
    main()
