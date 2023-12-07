import logging

class loggerDemo:
    def sample_logger(self):
        ##create logger
        logger=logging.getLogger("demolog")
        #set the level of logging
        logger.setLevel(logging.DEBUG)
        #create console handler or file handler
        ch=logging.StreamHandler
        #create formatter
        formatter=logging.Formatter('%(asctime)s - %(levelname)s - %(name)s :%(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        #add formatter to console or file formatter
        ch.setFormatter(formatter)
        #add console handler to the logger
        logger.addHandler(ch)
        #application code log messages
        logger.critical("this is critical log")
        logger.error("this is error log")
        logger.debug("this is debug log")
        logger.warning("this is warning log")
        logger.info("this is info log")
        logger.info("this is info2 log")

ld=loggerDemo()
ld.sample_logger()