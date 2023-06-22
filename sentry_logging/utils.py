import ast
import inspect
import sentry_sdk

# adapted from https://github.com/getsentry/sentry-python/issues/610

def log_function_with_sentry(wrapped, sentry_client):
    """Attaches Sentry integrations to a function."""
   
    def wrapper(*args, **kwargs):
       
        with sentry_client:
            try:
                 return  wrapped(*args, **kwargs)
            except Exception as e:
                sentry_sdk.capture_exception(e)
                sentry_client.flush()
                raise
    return  wrapper


def log_module_with_sentry(module=None, sentry_client=None):
    """Attaches Sentry integrations to a module."""
    module = module or inspect.getmodule(inspect.stack()[1][0])
    sentry_client = sentry_client or sentry_sdk.Hub(sentry_sdk.Client(dsn="..."))
    source_lines, _ = inspect.getsourcelines(module)
    source_code = ''.join(source_lines)

    module_ast = ast.parse(source_code)
    for node in module_ast.body:
        if isinstance(node, ast.ClassDef):
            cls = getattr(module, node.name)
            for key, value in cls.__dict__.items():
                if callable(value) or isinstance(value, (classmethod, staticmethod)):
                    setattr(cls, key, log_function_with_sentry(value, sentry_client))
        elif isinstance(node, (ast.AsyncFunctionDef, ast.FunctionDef)):
            setattr(module, node.name, log_function_with_sentry(getattr(module, node.name), sentry_client))



def sentry_trace(func): 
    
    def wrapper(*args, **kwargs):
        transaction = sentry_sdk.Hub.current.scope.transaction
       

        if transaction: 
            with transaction.start_child(op=func.__name__): 
                return func(*args, **kwargs) 
        else: 
            with sentry_sdk.start_transaction(op=func.__name__, name=func.__name__):
                return func(*args, **kwargs) 
    return wrapper