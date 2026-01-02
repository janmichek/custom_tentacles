#  Custom OctoBot Web Interface
#  A custom web interface tentacle with a bold green header
#  NO jinja2 needed - injects CSS directly into responses

import os
import flask

import tentacles.Services.Interfaces.web_interface.web as web_interface_web


class CustomWebInterface(web_interface_web.WebInterface):
    """
    Custom Web Interface with a bold green header.
    Extends the default WebInterface and injects custom CSS.
    """

    # Inline CSS for the green header - no external files needed!
    CUSTOM_CSS = """
    <style id="custom-web-interface-styles">
    /* BOLD GREEN HEADER */
    #main-nav-bar {
        background: linear-gradient(135deg, #00c853 0%, #1b5e20 50%, #004d40 100%) !important;
        box-shadow: 0 4px 20px rgba(0, 200, 83, 0.4) !important;
        border-bottom: 3px solid #69f0ae !important;
    }
    .navbar-brand {
        color: #ffffff !important;
        font-weight: 900 !important;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3) !important;
    }
    #main-nav-bar .nav-link {
        color: #e8f5e9 !important;
        font-weight: 600 !important;
    }
    #main-nav-bar .nav-link:hover {
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(255, 255, 255, 0.8) !important;
    }
    #main-nav-bar .nav-item.active {
        border-bottom: 3px solid #69f0ae !important;
    }
    #navbar-bot-status, #main-nav-bar .nav-link i {
        color: #b9f6ca !important;
    }
    /* GREEN FOOTER */
    footer.page-footer {
        background: linear-gradient(135deg, #1b5e20 0%, #004d40 100%) !important;
        color: #e8f5e9 !important;
        border-top: 3px solid #69f0ae !important;
    }
    footer.page-footer a {
        color: #b9f6ca !important;
    }
    </style>
    """

    def init_flask_plugins_and_config(self, server_instance):
        # Call parent's init
        super().init_flask_plugins_and_config(server_instance)

        # Inject our custom CSS into every HTML response
        @server_instance.after_request
        def inject_custom_css(response):
            if response.content_type and 'text/html' in response.content_type:
                # Inject CSS right before </head>
                data = response.get_data(as_text=True)
                if '</head>' in data:
                    data = data.replace('</head>', f'{self.CUSTOM_CSS}</head>')
                    response.set_data(data)
            return response
