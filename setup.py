from setuptools import find_packages, setup

setup(
    name="wildfire_forecasting",  # you should change "wildfire_forecasting" to your project name
    version="0.0.0",
    description="Code for paper Wildfire Danger Prediction and Understanding with Deep Learning",
    author="Ioannis Prapas, Spyros Kondylatos",
    author_email="",
    url="https://github.com/Orion-AI-Lab/daily-wildfire-danger",
    install_requires=["pytorch-lightning>=1.2.0", "hydra-core>=1.0.6", "torch==1.11.0", "torchvision==0.12.0",
                      "pytorch-lightning==1.5.8", "fastai==2.7.8"],
    packages=find_packages(),
)
