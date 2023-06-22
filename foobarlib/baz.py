import sentry_logging.clients as clients
import sentry_logging.utils as utils

@utils.sentry_trace
def compute_average(numbers):
    """Computes the average of a list of numbers."""
    raise Exception("baz could't compute average")
    # return sum(numbers) / len(numbers)

def compute_square(number):
    """Computes the square of a given number."""
    return number ** 2

utils.log_module_with_sentry(sentry_client=clients.sentry_client_b)