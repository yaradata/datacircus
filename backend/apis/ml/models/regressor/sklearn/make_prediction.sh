curl -X 'POST' \
  'http://ec2-3-93-13-166.compute-1.amazonaws.com:8070/regressor/processs' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "data_url": "static/504eae03-a3f0-41f3-91db-f641b505a64b#1987.csv",
  "data_sep": ",",
  "label": "ArrTime"
}'