import logging
logging.basicConfig(filename="log.txt", level =logging.WARNING, filemode="w")
print("Logging Demo")
logging.debug("Debug information")
logging.info("info information")
logging.warning("warning information")