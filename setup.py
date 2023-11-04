from setuptools import setup, find_namespace_packages

setup(
    name="bot_assistance",
    version="1.0.1",
    description="Very useful code",
    url="https://github.com/philipps777/MCS3-NeoU_Tech_Crew-bot_assistance",
    author="SITE",
    license="MIT",
    packages=find_namespace_packages(),
    install_requires=["prompt_toolkit"],
    entry_points={"console_scripts": [
        "NeoU_Tech_Crew-goitneo-python-project-team-13=main:main"]},
    include_package_data=True,
)
