get_comment() {
	
	csv='.csv'
	csv_name=$2$csv
	json='.json'
	json_name=$2$json
	
	python downloader.py --youtubeid $1 --output $json_name
	sed -i bak -e '1s/^/[ /' $json_name
	sed -i bak -e 's/}/},/g' $json_name
	sed -i bak -e '$ s/.$//' $json_name
	echo "]" >> $json_name

	python json_to_csv.py $json_name $csv_name

}

INPUT=$1
IFS=,
[ ! -f $INPUT ] && { echo "$INPUT file not found"; exit 99; }
while read movie_id videoIDs
do
	get_comment $videoIDs $movie_id 
done < $INPUT
IFS=,