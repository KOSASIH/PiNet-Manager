from lib.core.config import Config
from lib.core.logger import Logger
from lib.gui.gui_app import GUIApp

def main():
    config = Config()
    logger = Logger()

    gui_app = GUIApp()
    gui_app.run()

if __name__ == '__main__':
    main()
