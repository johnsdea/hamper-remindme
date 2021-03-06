from setuptools import setup

with open('requirements.txt') as f:
    requirements = [l.strip() for l in f]

setup(
    name='hamper_remindme',
    version='1.2',
    packages=['hamper_remindme'],
    author='Dean Johnson',
    author_email='deanjohnson222@gmail.com',
    url='https://github.com/dean/hamper-remindme',
    install_requires=requirements,
    package_data={'hamper-remindme': ['requirements.txt', 'README.md', 'LICENSE']},
    entry_points={
        'hamperbot.plugins': [
            'remindme = hamper_remindme.remindme:Reminder',
        ],
    },
)
