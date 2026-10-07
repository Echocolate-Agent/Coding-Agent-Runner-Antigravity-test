import inspect
import unittest

from src import task

FUNCTION_NAME = "normalize_whitespace"
PARAMETERS = ("text",)


class BaselineSmokeTests(unittest.TestCase):
    def test_function_and_signature(self):
        function = getattr(task, FUNCTION_NAME)
        self.assertTrue(callable(function))
        self.assertEqual(
            tuple(inspect.signature(function).parameters),
            PARAMETERS,
        )