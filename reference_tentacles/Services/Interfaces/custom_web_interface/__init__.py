#  Custom OctoBot Web Interface
#  A custom web interface tentacle with a bold green header

import octobot_commons.constants as commons_constants
if not commons_constants.USE_MINIMAL_LIBS:
    from tentacles.Services.Interfaces.custom_web_interface.web import CustomWebInterface

