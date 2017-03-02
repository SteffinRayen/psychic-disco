import os

from distutils.core import setup


base_path = os.path.dirname(os.path.abspath(__file__))
requirements_path = os.path.join(base_path, "setup", "requirements.txt")
reqs = [line.strip() for line in open(requirements_path)]


setup(
    name="sentiment-analysis-movie-review",
    version="0.1",
    description="Sentiment Analysis on Movie Reviews",
    author="Steffin Rayen",
    packages=["samr"],
    install_requires=reqs,
    scripts=["scripts/generate_result.py",
             "scripts/cross_validate_config.py",
             "scripts/download_3rdparty_data.py"]
)
