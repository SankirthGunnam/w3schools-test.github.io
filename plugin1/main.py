from gui import *


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    print("This is simple application main function")
    main_window = QtWidgets.QMainWindow()
    tabs = QtWidgets.QTabWidget()

    home_tab = QtWidgets.QWidget()
    home_tab.setLayout(QtWidgets.QVBoxLayout())

    welcome_message = QtWidgets.QLabel('<h1>Welcome to simple application to demonstrate plugin</h1>')
    welcome_message.setStyleSheet('background-color: orange; border-radius:5px;')
    home_tab.layout().addWidget(welcome_message)

    tabs.addTab(home_tab, 'Home')
    main_window.setCentralWidget(tabs)
    plugin_window = start_app()
    tabs.addTab(plugin_window, plugin_window.windowTitle())
    main_window.show()
    app.exec_()