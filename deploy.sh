#!/bin/bash
uploadfile="$1"
checkfile=".deploycheck"
target="/flash/main.py"

echo "Deploying $1 as $target ..."

if [[ ! -f "$uploadfile" ]]; then
	echo "Source not found, quitting."
	exit 1
fi
if [[ -f "$checkfile" ]]; then
	echo "Whoops, leftover check file $checkfile - remove manually and deploy again."
	exit 1
fi
export AMPY_PORT=/dev/ttyUSB0
echo -n "Uploading... "
ampy put "$1" "$target"
echo "OK"
echo -n "Verifying... "
ampy get "$target" "$checkfile"
diff --strip-trailing-cr "$uploadfile" "$checkfile" > /dev/null
if [ $? -eq 0 ]; then
	echo "OK"
	echo "Rebooting!"
	ampy reset --hard
else
	echo "FAIL!"
fi
rm "$checkfile"
