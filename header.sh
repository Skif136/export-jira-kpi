#! /bin/sh

CONTENT=`cat metric`

echo "HTTP/1.0 200 OK"
echo "Content-Length: ${#CONTENT}"
echo "Content-Type: text/plain; charset=utf-8"
echo ""
echo "${CONTENT}"