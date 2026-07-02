from app import create_app, db


def test_app_creates():
    app = create_app()
    assert app is not None


def test_db_tables_exist():
    app = create_app()
    with app.app_context():
        inspector = db.inspect(db.engine)
        tables = inspector.get_table_names()
        assert "user" in tables
        assert "post" in tables
