'''
    Execute pylint and check if the rating is 10.0.

    Raises:
        Exception: If the rating is lower than 10.0.
'''
from pylint.lint import Run

results = Run(['authentication', 'tests'], exit=False)
if results.linter.stats.global_note != 10.0:
    raise Exception('linter errors')
