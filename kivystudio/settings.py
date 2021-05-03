import os
from kivy.event import EventDispatcher
from kivy.config import ConfigParser
from kivy.properties import ConfigParserProperty
from kivystudio.tools import get_user_data_dir
from kivy.core.window  import Window

Window.maximize()

config = ConfigParser('kivystudio')
config.adddefaultsection('application')
config.adddefaultsection('graphics')
config_file = os.path.join(get_user_data_dir('kivystudio'), 'config.ini')
config.read(config_file)

class SettingDispatcher(EventDispatcher):

    auto_save = ConfigParserProperty(0, 'application', 'auto_save', 'kivystudio',val_type=int)

    auto_emulate = ConfigParserProperty(1, 'application', 'auto_emulate', 'kivystudio',val_type=int)

    dpi_scale = ConfigParserProperty(1, 'graphics', 'dpi_scale', 'kivystudio',val_type=float)

settings_obj = SettingDispatcher()
