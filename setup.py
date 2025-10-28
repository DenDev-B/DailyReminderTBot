from setuptools import setup, find_packages

setup(
    name="reminder_bot",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "aiogram==3.22.0",
        "aiohttp==3.12.15",
        "python-dotenv==1.2.1",
        "pytz==2024.1",
    ],
)