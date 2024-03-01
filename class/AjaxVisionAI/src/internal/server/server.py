from internal.router.route import Route
from internal.driver.mysql import MySQLConn
import os

DEFAULT_PORT="8080"
DEFAULT_HOST="0.0.0.0"

class Server:
    def __init__(self) -> None:
        self.port = os.environ.get("PORT", DEFAULT_PORT)
        self.host = os.environ.get("HOST", DEFAULT_HOST)
        
        dbconn = MySQLConn(
            host=os.environ.get("DB_HOST"),
            port=os.environ.get("DB_PORT"),
            user=os.environ.get("DB_USER"),
            passwd=os.environ.get("DB_PASSWORD"),
            db=os.environ.get("DB_NAME")
        )
        dbconn.connect()
        
        self.app = Route(dbconn=dbconn).New()
    
    def run(self) -> Exception:
        try:
            self.app.run(host=self.host, port=self.port, debug=True)
        except Exception as err:
            return err
