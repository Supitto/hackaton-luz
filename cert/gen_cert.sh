openssl genrsa -out cert.key 2048
openssl req -new -x509 -key cert.key -out cert.crt
cat cert.key cert.crt > cert.pem
openssl pkcs12 -export -in cert.pem -inkey cert.key -out server.p12