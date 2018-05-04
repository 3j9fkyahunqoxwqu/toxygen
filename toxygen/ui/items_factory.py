from ui.list_items import *
from ui.messages_widgets import *

# rename methods


class ItemsFactory:

    def __init__(self, settings, plugin_loader, smiley_loader, main_screen):
        self._settings, self._plugin_loader = settings, plugin_loader
        self._smiley_loader = smiley_loader
        self._messages = main_screen.messages
        self._friends_list = main_screen.friends_list
        self._message_edit = main_screen.messageEdit

    def friend_item(self):
        item = ContactItem(self._settings)
        elem = QtWidgets.QListWidgetItem(self._friends_list)
        elem.setSizeHint(QtCore.QSize(250, item.height()))
        self._friends_list.addItem(elem)
        self._friends_list.setItemWidget(elem, item)
        return item

    def message_item(self, message, append=True, pixmap=None):
        item = MessageItem(self._settings, self._create_message_browser, message, self._messages)
        if pixmap is not None:
            item.set_avatar(pixmap)
        elem = QtWidgets.QListWidgetItem()
        elem.setSizeHint(QtCore.QSize(self._messages.width(), item.height()))
        if append:
            self._messages.addItem(elem)
        else:
            self._messages.insertItem(0, elem)
        self._messages.setItemWidget(elem, item)
        return item

    def inline_item(self, data, append):
        elem = QtWidgets.QListWidgetItem()
        item = InlineImageItem(data, self._messages.width(), elem)
        elem.setSizeHint(QtCore.QSize(self._messages.width(), item.height()))
        if append:
            self._messages.addItem(elem)
        else:
            self._messages.insertItem(0, elem)
        self._messages.setItemWidget(elem, item)
        return item

    def unsent_file_item(self, file_name, size, name, time, append):
        item = UnsentFileItem(file_name,
                              size,
                              name,
                              time,
                              self._messages.width())
        elem = QtWidgets.QListWidgetItem()
        elem.setSizeHint(QtCore.QSize(self._messages.width() - 30, 34))
        if append:
            self._messages.addItem(elem)
        else:
            self._messages.insertItem(0, elem)
        self._messages.setItemWidget(elem, item)
        return item

    def file_transfer_item(self, data, append):
        data.append(self._messages.width())
        item = FileTransferItem(*data)
        elem = QtWidgets.QListWidgetItem()
        elem.setSizeHint(QtCore.QSize(self._messages.width() - 30, 34))
        if append:
            self._messages.addItem(elem)
        else:
            self._messages.insertItem(0, elem)
        self._messages.setItemWidget(elem, item)
        return item

    def _create_message_browser(self, text, width, message_type, parent=None):
        return MessageBrowser(self._settings, self._message_edit, self._smiley_loader, self._plugin_loader,
                              text, width, message_type, parent)
