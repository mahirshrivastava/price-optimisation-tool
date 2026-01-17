from price_optimization_tool import app
from price_optimization_tool.models import db

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=False)