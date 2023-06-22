### Sentry multi client
---
Details a potential implementation of Sentry using different clients for various modules within a library. Based off of this [discussion](https://github.com/getsentry/sentry-python/issues/610). 

### Setup
---
Add DSNs & client configurations corresponding to Sentry projects in `./sentry_logging/clients.py`

`python3 example.py`

### Limitations
---
This approach has only started to implement tracing on top of the multi client solution to errors. This has not been fully vetted yet.