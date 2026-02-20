import ctypes
import platform

DARK_THEME = """
QWidget {
    background-color: #2b2b2b;
    color: #d0d0d0;
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 10pt;
}

/* Кнопки */
QPushButton {
    background-color: #3c3c3c;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 6px 12px;
    margin: 2px;
}
QPushButton:hover {
    background-color: #4a4a4a;
    border: 1px solid #666;
}
QPushButton:pressed {
    background-color: #5a5a5a;
}
QPushButton:disabled {
    background-color: #2d2d2d;
    color: #6a6a6a;
    border: 1px solid #444;
}

/* Текстовые поля */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #252525;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 4px;
    selection-background-color: #3d6c8d;
}
QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #4a9eff;
}

/* Выпадающие списки */
QComboBox {
    background-color: #252525;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 4px 6px;
}
QComboBox:hover {
    border: 1px solid #666;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #555;
}
QComboBox::down-arrow {
    image: url(down_arrow.png); /* Замените на свою иконку или ударите строку */
}
QComboBox QAbstractItemView {
    background-color: #252525;
    border: 1px solid #555;
    selection-background-color: #3d6c8d;
}

/* Списки и таблицы */
QListView, QTreeView, QTableView {
    background-color: #252525;
    border: 1px solid #555;
    border-radius: 4px;
    alternate-background-color: #2e2e2e;
    selection-background-color: #3d6c8d;
}
QHeaderView::section {
    background-color: #353535;
    color: #d0d0d0;
    padding: 6px;
    border: 1px solid #555;
}

/* Вкладки */
QTabWidget::pane {
    border: 1px solid #555;
    background-color: #2b2b2b;
}
QTabBar::tab {
    background-color: #353535;
    color: #d0d0d0;
    padding: 8px 16px;
    margin-right: 2px;
}
QTabBar::tab:hover {
    background-color: #4a4a4a;
}
QTabBar::tab:selected {
    background-color: #2b2b2b;
    border-bottom: 2px solid #4a9eff;
}

/* Полосы прокрутки */
QScrollBar:vertical, QScrollBar:horizontal {
    background-color: #2b2b2b;
    width: 16px;
    height: 16px;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #555;
    border-radius: 8px;
    min-height: 30px;
    min-width: 30px;
}
QScrollBar::handle:hover {
    background-color: #666;
}
QScrollBar::add-line, QScrollBar::sub-line {
    background: none;
    border: none;
}

/* Чекбоксы и радио-кнопки */
QCheckBox, QRadioButton {
    spacing: 8px;
}
QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
}
QCheckBox::indicator {
    border: 1px solid #555;
    border-radius: 3px;
    background-color: #252525;
}
QCheckBox::indicator:checked {
    background-color: #4a9eff;
    image: url(checkmark.png); /* Замените на свою иконку */
}
QRadioButton::indicator {
    border: 1px solid #555;
    border-radius: 8px;
    background-color: #252525;
}
QRadioButton::indicator:checked {
    background-color: #4a9eff;
    border: 4px solid #252525;
}

/* Слайдеры */
QSlider::groove:horizontal {
    height: 6px;
    background-color: #555;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background-color: #4a9eff;
    width: 16px;
    height: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

/* Прогресс-бар */
QProgressBar {
    background-color: #252525;
    border: 1px solid #555;
    border-radius: 4px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #4a9eff;
    border-radius: 4px;
}

/* Групповые рамки */
QGroupBox {
    border: 1px solid #555;
    border-radius: 5px;
    margin-top: 12px;
    padding-top: 12px;
    font-weight: bold;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 6px;
}

/* Меню */
QMenuBar {
    background-color: #2b2b2b;
    color: #d0d0d0;
}
QMenuBar::item:selected {
    background-color: #4a9eff;
}
QMenu {
    background-color: #2b2b2b;
    border: 1px solid #555;
}
QMenu::item:selected {
    background-color: #3d6c8d;
}

/* Разделители */
QSplitter::handle {
    background-color: #555;
}
QSplitter::handle:hover {
    background-color: #666;
}

/* Подсказки */
QToolTip {
    background-color: #353535;
    color: #d0d0d0;
    border: 1px solid #555;
    border-radius: 4px;
}

/* Статус-бар */
QStatusBar {
    background-color: #252525;
    color: #d0d0d0;
}
"""

MORE_DARK_THEME = """
QWidget {
    background-color: #1e1e1e;  /* было #2b2b2b */
    color: #c0c0c0;             /* было #d0d0d0 */
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 10pt;
}

/* Кнопки */
QPushButton {
    background-color: #2a2a2a;  /* было #3c3c3c */
    border: 1px solid #3a3a3a;  /* было #555 */
    border-radius: 4px;
    padding: 6px 12px;
    margin: 2px;
}
QPushButton:hover {
    background-color: #3a3a3a;  /* было #4a4a4a */
    border: 1px solid #4a4a4a;  /* было #666 */
}
QPushButton:pressed {
    background-color: #4a4a4a;  /* было #5a5a5a */
}
QPushButton:disabled {
    background-color: #252525;  /* было #2d2d2d */
    color: #6a6a6a;
    border: 1px solid #3a3a3a;  /* было #444 */
}

/* Текстовые поля */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #1a1a1a;  /* было #252525 */
    border: 1px solid #3a3a3a;  /* было #555 */
    border-radius: 4px;
    padding: 4px;
    selection-background-color: #3d6c8d;
}
QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #4a9eff;  /* оставим яркий акцент */
}

/* Выпадающие списки */
QComboBox {
    background-color: #1a1a1a;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    padding: 4px 6px;
}
QComboBox:hover {
    border: 1px solid #4a4a4a;  /* было #666 */
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #3a3a3a;  /* было #555 */
}
QComboBox::down-arrow {
    image: url(down_arrow.png); /* замените на свою иконку */
}
QComboBox QAbstractItemView {
    background-color: #1a1a1a;
    border: 1px solid #3a3a3a;
    selection-background-color: #3d6c8d;
}

/* Списки и таблицы */
QListView, QTreeView, QTableView {
    background-color: #1a1a1a;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    alternate-background-color: #252525;  /* было #2e2e2e */
    selection-background-color: #3d6c8d;
}
QHeaderView::section {
    background-color: #2a2a2a;  /* было #353535 */
    color: #c0c0c0;
    padding: 6px;
    border: 1px solid #3a3a3a;
}

/* Вкладки */
QTabWidget::pane {
    border: 1px solid #3a3a3a;
    background-color: #1e1e1e;
}
QTabBar::tab {
    background-color: #2a2a2a;
    color: #c0c0c0;
    padding: 8px 16px;
    margin-right: 2px;
}
QTabBar::tab:hover {
    background-color: #3a3a3a;
}
QTabBar::tab:selected {
    background-color: #1e1e1e;
    border-bottom: 2px solid #4a9eff;
}

/* Полосы прокрутки */
QScrollBar:vertical, QScrollBar:horizontal {
    background-color: #1e1e1e;
    width: 16px;
    height: 16px;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #3a3a3a;  /* было #555 */
    border-radius: 8px;
    min-height: 30px;
    min-width: 30px;
}
QScrollBar::handle:hover {
    background-color: #4a4a4a;  /* было #666 */
}
QScrollBar::add-line, QScrollBar::sub-line {
    background: none;
    border: none;
}

/* Чекбоксы и радио-кнопки */
QCheckBox, QRadioButton {
    spacing: 8px;
}
QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
}
QCheckBox::indicator {
    border: 1px solid #3a3a3a;
    border-radius: 3px;
    background-color: #1a1a1a;
}
QCheckBox::indicator:checked {
    background-color: #4a9eff;
    image: url(checkmark.png); /* замените на свою иконку */
}
QRadioButton::indicator {
    border: 1px solid #3a3a3a;
    border-radius: 8px;
    background-color: #1a1a1a;
}
QRadioButton::indicator:checked {
    background-color: #4a9eff;
    border: 4px solid #1a1a1a;
}

/* Слайдеры */
QSlider::groove:horizontal {
    height: 6px;
    background-color: #3a3a3a;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background-color: #4a9eff;
    width: 16px;
    height: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

/* Прогресс-бар */
QProgressBar {
    background-color: #1a1a1a;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #4a9eff;
    border-radius: 4px;
}

/* Групповые рамки */
QGroupBox {
    border: 1px solid #3a3a3a;
    border-radius: 5px;
    margin-top: 12px;
    padding-top: 12px;
    font-weight: bold;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 6px;
}

/* Меню */
QMenuBar {
    background-color: #1e1e1e;
    color: #c0c0c0;
}
QMenuBar::item:selected {
    background-color: #4a9eff;
}
QMenu {
    background-color: #1e1e1e;
    border: 1px solid #3a3a3a;
}
QMenu::item:selected {
    background-color: #3d6c8d;
}

/* Разделители */
QSplitter::handle {
    background-color: #3a3a3a;
}
QSplitter::handle:hover {
    background-color: #4a4a4a;
}

/* Подсказки */
QToolTip {
    background-color: #2a2a2a;
    color: #c0c0c0;
    border: 1px solid #3a3a3a;
    border-radius: 4px;
}

/* Статус-бар */
QStatusBar {
    background-color: #1a1a1a;
    color: #c0c0c0;
}
"""

EXTRA_DARK_THEME = """
QWidget {
    background-color: #0f0f0f;   /* основной фон — глубокий чёрный */
    color: #e0e0e0;              /* светло-серый текст для контраста */
    font-family: 'Segoe UI', Arial, sans-serif;
    font-size: 10pt;
}

/* Кнопки */
QPushButton {
    background-color: #1f1f1f;   /* чуть светлее фона */
    border: 1px solid #2a2a2a;
    border-radius: 4px;
    padding: 6px 12px;
    margin: 2px;
}
QPushButton:hover {
    background-color: #2a2a2a;   /* светлее при наведении */
    border: 1px solid #3a3a3a;
}
QPushButton:pressed {
    background-color: #333333;   /* ещё светлее при нажатии */
}
QPushButton:disabled {
    background-color: #1a1a1a;
    color: #6a6a6a;
    border: 1px solid #2a2a2a;
}

/* Текстовые поля */
QLineEdit, QTextEdit, QPlainTextEdit {
    background-color: #141414;   /* чуть темнее кнопок, но не основной */
    border: 1px solid #2a2a2a;
    border-radius: 4px;
    padding: 4px;
    selection-background-color: #3d6c8d;
}
QLineEdit:focus, QTextEdit:focus, QPlainTextEdit:focus {
    border: 1px solid #4a9eff;   /* яркий акцент при фокусе */
}

/* Выпадающие списки */
QComboBox {
    background-color: #141414;
    border: 1px solid #2a2a2a;
    border-radius: 4px;
    padding: 4px 6px;
}
QComboBox:hover {
    border: 1px solid #3a3a3a;
}
QComboBox::drop-down {
    subcontrol-origin: padding;
    subcontrol-position: top right;
    width: 20px;
    border-left: 1px solid #2a2a2a;
}
QComboBox::down-arrow {
    image: url(down_arrow.png);
}
QComboBox QAbstractItemView {
    background-color: #141414;
    border: 1px solid #2a2a2a;
    selection-background-color: #3d6c8d;
}

/* Списки и таблицы */
QListView, QTreeView, QTableView {
    background-color: #141414;
    border: 1px solid #2a2a2a;
    border-radius: 4px;
    alternate-background-color: #1a1a1a;
    selection-background-color: #3d6c8d;
}
QHeaderView::section {
    background-color: #1f1f1f;
    color: #e0e0e0;
    padding: 6px;
    border: 1px solid #2a2a2a;
}

/* Вкладки */
QTabWidget::pane {
    border: 1px solid #2a2a2a;
    background-color: #0f0f0f;
}
QTabBar::tab {
    background-color: #1f1f1f;
    color: #e0e0e0;
    padding: 8px 16px;
    margin-right: 2px;
}
QTabBar::tab:hover {
    background-color: #2a2a2a;
}
QTabBar::tab:selected {
    background-color: #0f0f0f;
    border-bottom: 2px solid #4a9eff;
}

/* Полосы прокрутки */
QScrollBar:vertical, QScrollBar:horizontal {
    background-color: #0f0f0f;
    width: 16px;
    height: 16px;
}
QScrollBar::handle:vertical, QScrollBar::handle:horizontal {
    background-color: #2a2a2a;
    border-radius: 8px;
    min-height: 30px;
    min-width: 30px;
}
QScrollBar::handle:hover {
    background-color: #3a3a3a;
}
QScrollBar::add-line, QScrollBar::sub-line {
    background: none;
    border: none;
}

/* Чекбоксы и радио-кнопки */
QCheckBox, QRadioButton {
    spacing: 8px;
}
QCheckBox::indicator, QRadioButton::indicator {
    width: 16px;
    height: 16px;
}
QCheckBox::indicator {
    border: 1px solid #2a2a2a;
    border-radius: 3px;
    background-color: #141414;
}
QCheckBox::indicator:checked {
    background-color: #4a9eff;
    image: url(checkmark.png);
}
QRadioButton::indicator {
    border: 1px solid #2a2a2a;
    border-radius: 8px;
    background-color: #141414;
}
QRadioButton::indicator:checked {
    background-color: #4a9eff;
    border: 4px solid #141414;
}

/* Слайдеры */
QSlider::groove:horizontal {
    height: 6px;
    background-color: #2a2a2a;
    border-radius: 3px;
}
QSlider::handle:horizontal {
    background-color: #4a9eff;
    width: 16px;
    height: 16px;
    margin: -5px 0;
    border-radius: 8px;
}

/* Прогресс-бар */
QProgressBar {
    background-color: #141414;
    border: 1px solid #2a2a2a;
    border-radius: 4px;
    text-align: center;
}
QProgressBar::chunk {
    background-color: #4a9eff;
    border-radius: 4px;
}

/* Групповые рамки */
QGroupBox {
    border: 1px solid #2a2a2a;
    border-radius: 5px;
    margin-top: 12px;
    padding-top: 12px;
    font-weight: bold;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 6px;
}

/* Меню */
QMenuBar {
    background-color: #0f0f0f;
    color: #e0e0e0;
}
QMenuBar::item:selected {
    background-color: #4a9eff;
}
QMenu {
    background-color: #0f0f0f;
    border: 1px solid #2a2a2a;
}
QMenu::item:selected {
    background-color: #3d6c8d;
}

/* Разделители */
QSplitter::handle {
    background-color: #2a2a2a;
}
QSplitter::handle:hover {
    background-color: #3a3a3a;
}

/* Подсказки */
QToolTip {
    background-color: #1f1f1f;
    color: #e0e0e0;
    border: 1px solid #2a2a2a;
    border-radius: 4px;
}

/* Статус-бар */
QStatusBar {
    background-color: #141414;
    color: #e0e0e0;
}
"""

def set_dark_title_bar(window):
    # DWMWA_USE_IMMERSIVE_DARK_MODE = 20
    # Эта константа говорит Windows включить темную тему для заголовка
    if platform.system() != "Windows":
        return
    try:
        # Пытаемся применить атрибут (работает на Windows 10 build 19041+ и Windows 11)
        hwnd = int(window.winId())
        value = ctypes.c_int(1) # 1 = включить, 0 = выключить
        ctypes.windll.dwmapi.DwmSetWindowAttribute(
            hwnd, 20, ctypes.byref(value), ctypes.sizeof(value)
        )
    except Exception as e:
        print(f"Не удалось применить темную тему: {e}")

def apply_dark_theme(window):
    window.setStyleSheet(EXTRA_DARK_THEME)
    set_dark_title_bar(window)