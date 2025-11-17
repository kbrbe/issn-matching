ENRICHED_PLACE="kbr/kbr-data-place-enriched.csv"
ENRICH_LOG="kbr/kbr-data-place-enriched.log"
INPUT_PLACE="kbr/kbr-data-place.csv"

python -m geoname_enrichment.geoname_enrichment \
  -c config-geoname.json \
  -p "place" \
  --id-column "autID" \
  --countryname-column "country" \
  -o $ENRICHED_PLACE \
  -l $ENRICH_LOG \
  $INPUT_PLACE


