from setuptools import setup

PACKAGE = 'Keepmail'
VERSION = '0.0.1'

setup(name=PACKAGE,
      version=VERSION,
      description="Keepmail is a mail server which keeps copies of email, but does not send them. It is useful for development and testing of applications which send email.",
      author="Robert Gravina",
      author_email="robert@gravina.com",
      url="http://github.com/keepmail",
      licence="MIT",
      packages=['keepmail'],
)
