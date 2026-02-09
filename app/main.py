import os
from pathlib import Path
from flask import Flask
from app.routes import main_routes


def create_app():
    base_dir = Path(__file__).resolve().parent.parent
    templates_dir = str(base_dir / "templates")
    static_dir = str(base_dir / "static")
    app = Flask(__name__, template_folder=templates_dir, static_folder=static_dir)
    
    # Enable session support
    app.secret_key = os.getenv("FLASK_SECRET_KEY", "dev-secret-key-change-in-production")
    
    # Add error handlers
    @app.errorhandler(500)
    def internal_error(error):
        print(f"[ERROR 500] {error}")
        return {"error": "Internal server error"}, 500
    
    @app.errorhandler(404)
    def not_found(error):
        print(f"[ERROR 404] {error}")
        return {"error": "Not found"}, 404
    
    app.register_blueprint(main_routes)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)


