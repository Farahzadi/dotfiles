PROXY_URL = "http://127.0.0.1:2081"

def apply_proxy_settings(config):
    # Default: proxy everything
    config.set("content.proxy", PROXY_URL)

    # Exceptions: .ir and snappfood
    exception_patterns = [
        "*://*.ir/*",
        "*://*snappfood*/*",
    ]
    for pat in exception_patterns:
        config.set("content.proxy", "system", pat)

    # Keybinds
    config.bind(",pe", f"set content.proxy {PROXY_URL} ;; message-info 'Proxy ON (except .ir, *snappfood*)'")
    config.bind(",pd", "set content.proxy system ;; message-info 'Proxy OFF (system)'")

