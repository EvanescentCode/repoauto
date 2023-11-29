import logging
import inspect
import softest


class Utils(softest.TestCase):
    @staticmethod
    def custom_logger(log_level=logging.DEBUG):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(log_level)
        handler = logging.FileHandler(filename='..\\reports\log.log')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                                      datefmt='%d-%m-%Y %H:%M:%S %p')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def assert_list_item(self, list_name, ass_value):
        log = self.custom_logger()
        for ass in list_name:
            log.info('Text is:' + ass.text)
            self.assertEqual(ass, ass_value)
            log.info('Assert Pass')

    def soft_assert_list_item(self, list_name, ass_value):
        log = self.custom_logger()
        for ass in list_name:
            log.info('Text is: ' + ass.text)
            self.soft_assert(self.assertEqual, ass, ass_value)
            log.info('Assert Pass')

    def soft_assert_item(self, item, ass_value):
        log = self.custom_logger()
        log.info('Text is' + ass_value.text)
        self.soft_assert(self.assertEqual, item, ass_value)
        log.info('Assert Pass')
