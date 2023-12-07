import logging

logging.basicConfig(level=logging.DEBUG, filemode="a", filename="gatherLog.log")

logging.critical("this is critical log")
logging.error("this is error log")
logging.debug("this is debug log")
logging.warning("this is warning log")
logging.info("this is info log")
logging.info("this is info2 log")