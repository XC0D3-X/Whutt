<?php
if(empty($argv[1]))
	exit("How to use : php ".$argv[0]." domain.txt\n");

if(!file_exists($argv[1])) {
	exit("File not found\n");
}

$f = file_get_contents($argv[1]);
if(empty($f))
	exit("Empty file\n");

$array = array();
$xp = explode("\n", $f);

for($i=0;$i<count($xp);$i++) {
	array_push($array, trim($xp[$i]));
}
$filtered = array_unique($array);

$f = fopen("filteredDomain.txt", "a+");
fwrite($f, implode("\n", $filtered));
fclose($f);
echo "Saved to filteredDomain.txt\n";
