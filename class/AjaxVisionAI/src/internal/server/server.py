from internal.router.route import newRoute
import os

DEFAULT_PORT="8080"
DEFAULT_HOST="0.0.0.0"

class Server:
    def __init__(self) -> None:
        self.port = os.environ.get("PORT", DEFAULT_PORT)
        self.host = os.environ.get("HOST", DEFAULT_HOST)
        
        self.app = newRoute()
    
    def run(self) -> Exception:
        try:
            self.app.run(host=self.host, port=self.port, debug=True)
        except Exception as err:
            return err
