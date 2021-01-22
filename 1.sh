path_dir="/home/fred/azure-rest-api-specs/specification"
for item in "$path_dir"/*
do
    echo "$path_dir"
    echo "$item"
    autorest --ansible --use=./  "$item"/resource-manager/readme.md  --log --ansible-output-folder=../tmp
done
echo " For test"
