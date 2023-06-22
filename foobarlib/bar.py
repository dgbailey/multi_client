import sentry_logging.clients as clients
import sentry_logging.utils as utils

@utils.sentry_trace
def read_file(filename):
    """Reads the contents of a file and returns it as a string."""
    with open(filename, 'r') as file:
        return file.read()

@utils.sentry_trace
def write_file(filename, content):
    """Writes the given content to a file."""
    with open(filename, 'w') as file:
        file.write(content)

utils.log_module_with_sentry(sentry_client=clients.sentry_client_a)