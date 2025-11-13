python -m xml_to_csv.xml_to_csv \
  -c extract-config-issn-plus.json \
  -d date-mapping.json \
  -p "issn-plus-data" \
  -l issn-plus/issn-plus-data.log \
  -L "DEBUG" \
  -o issn-plus/issn-plus-data.csv \
  exportissn+.xml
