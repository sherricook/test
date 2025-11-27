"""
Test cases to verify the functionality of linux commands
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path
from typing import NamedTuple

import pytest
from _pytest.fixtures import SubRequest


class Command(NamedTuple):
    """
    Command Tuple
    """

    description: str = ''
    cmd: str = ''


CMD_HELLO_WORLD = Command(
    description='Print Hello, World!',
    cmd=r'echo Hello, World!',
)

CMD_HELLO_SHERRI = Command(
    description='Print Hello, Sherri!',
    cmd=r'echo Hello, Sherri!',
)


def configure_logging(logger_name: str):
    # create a logger object
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    # log format: [11-08-2025 20:03:46 INFO] This is my formatted message
    formatter = logging.Formatter(
        fmt='[%(asctime)s %(levelname)s] %(message)s',
        datefmt='%m-%d-%Y %H:%M:%S',
    )

    # console logger
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    # file logger
    logs_dir = Path.cwd() / "logs"
    logs_dir.mkdir(exist_ok=True)
    file_handler = RotatingFileHandler(
        filename=logs_dir / f'{logger_name}.log',
        mode='a',
        encoding='utf-8',
        maxBytes=10000000,
        backupCount=3,
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


LOG = configure_logging(__name__)


@pytest.fixture(scope='function')
def command(request: SubRequest):
    """
    Fixture to check command prerequisite
    :param request: pytest SubRequest object to get test params
    """
    command_info = request.param
    print(command_info)
    yield command_info


@pytest.mark.parametrize(
    'command',
    [
        pytest.param(
            CMD_HELLO_WORLD,
            id=CMD_HELLO_WORLD.description,
        ),
        pytest.param(
            CMD_HELLO_SHERRI,
            id=CMD_HELLO_SHERRI.description,
        ),
    ],
    indirect=['command'],
)
class TestCommand:
    """
    Command test cases
    """

    @pytest.mark.linux_only
    def test_command(
        self,
        command: Command,
    ):
        """
        Verify linux commands
        :param command test various commands
        """
        LOG.info(command.description)
        LOG.info(command.cmd)
