from setuptools import setup, find_packages

setup(
    name="testcloud",
    packages=["testcloud","testcloud.routes", "testcloud.registration_user", "testcloud.uploading_files"],
    version="0.0.1",
    install_requires=["fastapi", "pydantic", "SQLAlchemy", "gunicorn",
                    "uvicorn", "python-dotenv", "asyncpg", "fastapi-users",
                    "fastapi-users-db-sqlalchemy", "alembic"],
)