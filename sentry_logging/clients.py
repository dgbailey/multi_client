import sentry_sdk

sentry_client_b = sentry_sdk.Hub(sentry_sdk.Client(dsn="...",debug=True,traces_sample_rate=1.0))
sentry_client_a = sentry_sdk.Hub(sentry_sdk.Client(dsn="...",traces_sample_rate=1.0))