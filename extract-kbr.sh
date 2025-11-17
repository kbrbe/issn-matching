python -m xml_to_csv.xml_to_csv \
  -c extract-config-kbr.json \
  -d date-mapping.json \
  -p "kbr-data" \
  -l kbr/kbr-data.log \
  -L "INFO" \
  -o kbr/kbr-data.csv \
  kbr-paper-periodicals.xml
