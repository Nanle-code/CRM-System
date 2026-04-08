#!/usr/bin/env python3
"""
Gunicorn configuration for production deployment
"""

bind = "0.0.0.0:5000"
workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2
max_requests = 1000
max_requests_jitter = 100
preload_app = True
daemon = False
user = None
group = None
tmp_upload_dir = None
errorlog = "-"
accesslog = "-"
loglevel = "info"

# Production settings
forwarded_allow_ips = "*"
secure_scheme_headers = {
    'X-Forwarded-Proto': 'https',
    'X-Forwarded-Host': 'localhost'
}
