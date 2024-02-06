import logging
import subprocess
import ctypes
import sys
import time
import webbrowser


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


def run_as_admin():
    if is_admin():
        return
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


def stop_spooler():
    try:
        logging.info("Stop print service...")
        subprocess.run(["net", "stop", "spooler"], check=True)
        time.sleep(3)
        logging.info("Print service successfully stopped.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error when stopping the print service: {e}")


def start_spooler():
    try:
        logging.info("Restart print service...")
        subprocess.run(["net", "start", "spooler"], check=True)
        time.sleep(3)
        logging.info("Print service successfully launched.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error when starting the print service: {e}")


def clear_print_queue():
    stop_spooler()

    '''
    # This block may be needed if the print queue isn't clear automatically while restarting the service

    try:
        logging.info("Lösche Druckerwarteschlange...")
        subprocess.run(["del", "/Q", "/F", "%systemroot%\\System32\\spool\\PRINTERS\\*"], check=True)
        logging.info("Druckerwarteschlange erfolgreich gelöscht.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Fehler beim Löschen der Druckerwarteschlange: {e}")
    '''

    start_spooler()


def main():
    logging.basicConfig(filename='logfile.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    run_as_admin()
    clear_print_queue()

    open_logfile_handler = logging.FileHandler('logfile.log')
    open_logfile_handler.setLevel(logging.DEBUG)
    open_logfile_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logging.getLogger().addHandler(open_logfile_handler)

    webbrowser.open('logfile.log', new=2)


if __name__ == "__main__":
    main()
