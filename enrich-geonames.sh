ENRICHED_PLACE="issn-plus/issn-plus-data-place-enriched.csv"
ENRICH_LOG="issn-plus/issn-plus-data-place-enriched.log"
INPUT_PLACE="issn-plus/issn-plus-data-place.csv"

python -m geoname_enrichment.geoname_enrichment \
  -c config-geoname.json \
  -p "place" \
  --id-column "autID" \
  --countryname-column "country" \
  -o $ENRICHED_PLACE \
  -l $ENRICH_LOG \
  $INPUT_PLACE


