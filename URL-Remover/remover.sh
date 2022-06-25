#!/bin/bash
remove(){
	delete=$(echo $1 | sed 's/https\?:\/\///' | sed 's/http\?:\/\///')
	printf "Remove HTTP/HTTPS => $1\n"
	echo "$delete">>$saved
}
cat << "EOF"
                      .".
                     /  |
                    /  /
                   / ,"
       .-------.--- /
      "._ __.-/ o. o\
         "   (    Y  )
              )     /
             /     (
            /       Y
        .-"         |
       /  _     \    \
      /    `. ". ) /' )
     Y       )( / /(,/
    ,|      /     )
   ( |     /     /
    " \_  (__   (__        [NakoCoders - Remove HTTP/HTTPS]
        "-._,)--._,)
EOF
echo ""
read -p "Select Your List : " listo;
read -p "Save Name (Name.txt) : " saved;

multithread_limit=7
IFS=$'\r\n' GLOBIGNORE='*' command eval 'list=($(cat $listo))'
for (( i = 0; i < "${#list[@]}"; i++ )); 
do
	target="${list[$i]}"
	((cthread=cthread%multithread_limit)); ((cthread++==0)) && wait
	remove ${target} ${saved}&
done
wait
