from config import Config
from main import create_app

config = Config()
app = create_app(config)

if __name__ == '__main__':
    app.run(port=16000)
