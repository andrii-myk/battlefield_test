import logging

FORMAT = "%(levelname)s %(asctime)s - %(message)s"

logging.basicConfig(filename='logger/battle.log',
                    level= logging.DEBUG,
                    format= FORMAT,
                    filemode= 'w')

logger = logging.getLogger()