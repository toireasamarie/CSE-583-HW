mkdir pronto
cd pronto
touch README.txt
echo "This holds the pronto data" > README.txt
mkdir data
cd data
touch amazondata.zip
curl  https://s3.amazonaws.com/pronto-data/open_data_year_one.zip > amazondata.zip
unzip amazondata.zip
head *.csv

