FROM mitmproxy/mitmproxy

ADD addon.py .


#CMD ls -la /*
CMD mitmproxy -s addon.py --certs *=/cert/cert.pem
