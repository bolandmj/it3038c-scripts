DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
TODAY=$(date)
NEGATIVE=$(echo $DATA | jq '.[0].negative')
POSITIVE=$(echo $DATA | jq '.[0].positive')
DEATH=$(echo $DATA | jq '.[0].death')


echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative COVID tests, and $DEATH deaths."

