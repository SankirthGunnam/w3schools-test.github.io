import os
import pickle
import sys
import importlib.util


# import PySide2
# from PySide2 import QtWidgets


def import_module_from_string(name: str, source: str):
    spec = importlib.util.spec_from_loader(name, loader=None)
    mod = importlib.util.module_from_spec(spec)
    exec(source, mod.__dict__)
    sys.modules[name] = mod
    globals()[name] = mod


def load_plugin(plugin_name):
    if not os.path.isfile(plugin_name):
        return False
    with open(plugin_name, 'rb') as fp:
        modules = pickle.load(fp)
        for name, module in modules.items():
            import_module_from_string(name, module)

    return True


if __name__ == '__main__':
    print('This is sample plugin1 main function')
    from PySide2 import QtWidgets

    app = QtWidgets.QApplication()
    main_window = QtWidgets.QMainWindow()
    tabs = QtWidgets.QTabWidget()

    home_tab = QtWidgets.QWidget()
    home_tab.setLayout(QtWidgets.QVBoxLayout())

    welcome_message = QtWidgets.QLabel('<h1>Welcome to simple application to demonstrate plugin</h1>')
    welcome_message.setStyleSheet('background-color: skyblue; border-radius:5px;')
    home_tab.layout().addWidget(welcome_message)

    tabs.addTab(home_tab, 'Home')
    main_window.setCentralWidget(tabs)

    if load_plugin('plugin.dll'):
        from gui import *
        plugin_window = start_app()
        tabs.addTab(plugin_window, plugin_window.windowTitle())

    main_window.setWindowTitle('Sample Application')
    main_window.setMinimumSize(800, 500)
    main_window.show()
    app.exec_()
