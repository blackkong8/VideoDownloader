read id

FILE=$(curl -sX POST https://vanfem.com/api/source/$id |\
python3 -c "import sys, json; print(json.load(sys.stdin)['data'][0]['file'])")
[[ -z "$FILE" ]] && { echo "FILE is empty" ; exit 1; }

URL=$(curl -Is $FILE | grep location | cut -c 11- | sed 's/.$//')
[[ -z "$URL" ]] && { echo "FILE is empty" ; exit 1; }

echo $URL

curl -C - -O $URL