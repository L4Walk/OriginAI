# coding:utf-8
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtGui import QPixmap, QPainter, QColor, QBrush, QPainterPath
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEngineProfile
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl

from qfluentwidgets import ScrollArea, isDarkTheme, FluentIcon
from ..common.config import cfg, HELP_URL, FEEDBACK_URL, AUTHOR, VERSION, YEAR, isWin11
from ..common.icon import Icon, FluentIconBase
from ..components.link_card import LinkCardView
from ..components.sample_card import SampleCardView
from ..common.style_sheet import StyleSheet

from time import sleep
from sys import argv, exit

"""
try:
    import pyi_splash
    pyi_splash.update_text('UI Loaded ...')
    sleep(3)
    pyi_splash.close()
except:
       pass
"""

class ChatInterface(ScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.scrollWidget = QWidget()
        # setting label
        self.settingLabel = QLabel("ChatGPT", self)

        self.profile = QWebEngineProfile('ChatGPTProfile')
        self.settings = self.profile.settings()
        self.webview = QWebEngineView(self.scrollWidget)  # 注意这里，我们将其父窗口设置为 self.scrollWidget
        self.webview.setGeometry(1200, 500, 600, 520)  # 设置webview的大小和位置
        self.webview.setZoomFactor(0.7)
        # self.url = QUrl("https://www.lanshankj.com/")
        self.url = QUrl("https://chat.openai.com/chat")
        self.webview.load(self.url)

        self.__initWidget()
        self.__initLayout()
        self.webview.show()

    def __initWidget(self):
        self.resize(1000, 800)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 80, 0, 20)
        self.setObjectName('chatInterface')
        self.setWidgetResizable(True)
        self.setObjectName('settingInterface')

        # initialize style sheet
        self.scrollWidget.setObjectName('scrollWidget')
        self.settingLabel.setObjectName('settingLabel')
        StyleSheet.SETTING_INTERFACE.apply(self)

        #self.micaCard.setEnabled(isWin11())

        # initialize layout
        #self.__initLayout()
        #self.__connectSignalToSlot()


    def __initLayout(self):
        #self.settingLabel.move(36, 30)
        layout = QVBoxLayout(self.scrollWidget)
        layout.addWidget(self.webview)
        self.scrollWidget.setLayout(layout)
        self.setWidget(self.scrollWidget)

