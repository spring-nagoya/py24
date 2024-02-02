from internal.router.route import initRoute
import os

DEFAULT_PORT="8080"
DEFAULT_HOST="0.0.0.0"

def server() -> Exception:
    port = os.environ.get("PORT", DEFAULT_PORT)
    host = os.environ.get("HOST", DEFAULT_HOST)
    
    app = initRoute()
    
    try:
        app.run(host=host, port=port, debug=True)
    except Exception as err:
        return err