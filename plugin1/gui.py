from PySide2 import QtWidgets, QtCore


def start_app():
    print("This is simple plugin start function")
    main_window = QtWidgets.QMainWindow()
    central_widget = QtWidgets.QWidget()
    central_widget.setLayout(QtWidgets.QVBoxLayout())
    editor = QtWidgets.QTextEdit()
    editor.setPlaceholderText('Type something here')
    central_widget.layout().addWidget(editor)

    logger = QtWidgets.QTextEdit()
    logger.setPlaceholderText('This is logger')
    logger.setEnabled(False)

    log_docker = QtWidgets.QDockWidget()
    log_docker.setWidget(logger)

    contents = QtWidgets.QListWidget()
    contents.addItems([f'file_{x + 1}.py' for x in range(100)])
    contents_docker = QtWidgets.QDockWidget()
    contents_docker.setWidget(contents)
    main_window.setCentralWidget(editor)
    main_window.addDockWidget(QtCore.Qt.BottomDockWidgetArea, log_docker)
    main_window.addDockWidget(QtCore.Qt.LeftDockWidgetArea, contents_docker)
    main_window.setMinimumSize(800, 500)
    main_window.setWindowTitle('Sample Plugin')
    return main_window