cloc ./ --by-file --csv --quiet --report-file=cloc_report.csv &&
cat cloc_report.csv |
while read row
do
	echo $(echo "$row" | awk -F',' '{print $2}');
	echo $(echo "$row" | awk -F',' '{print $1}');
	git log --pretty=format:%an -- $FILE | sort -u;
	echo "";
done
