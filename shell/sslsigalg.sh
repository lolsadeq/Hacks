#!/bin/bash
 
EXPIRES=`echo | openssl s_client -showcerts -connect $1:443 2>/dev/null | openssl x509 -inform pem -noout -dates | grep notAfter | cut -d'=' -f2`
SIGALGO=`echo | openssl s_client -showcerts -connect $1:443 2>/dev/null | openssl x509 -inform pem -noout -text | grep 'Signature Alg' | cut -d':' -f2 | head -n1`
 
printf "%s: %s -%s\n" "$1" "$EXPIRES" "$SIGALGO"
