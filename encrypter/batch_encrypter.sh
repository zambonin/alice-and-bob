#!/bin/bash

python id_fetcher.py

alunos=($(cat "temp")) && rm "temp"

for (( i = 0; i < ${#alunos[@]}; ++i )); do
echo "$RANDOM $RANDOM" > "${alunos[i]}.txt"
nozero=$(echo ${alunos[i]} | sed 's/^0*//')
key=$RANDOM
echo $(( $nozero * $key )) \
    | gpg --batch --passphrase-fd 0 -c "${alunos[i]}.txt"
done

tar czf "encrypted.tar.gz" *.gpg
rm *.{txt,gpg}
echo "Use com sabedoria: $key"
