@heads = qw/locationDbId	altern	local	crops	cont	creg	adm3	adm2	adm1	annualTotalPrecipitation	annualMeanTemperature/;
$l = 0;
while(<>) {
    $l++;
    next if ($l == 1);
    chomp;
	@f = split('\t');
    $id = shift(@f);
	@f2 = ();
    $i = 1;
    foreach $f1 (@f) {
		push(@f2, '"' . $heads[$i] . '": "' . $f1 . '"');
        $i++;
	}
    print($id . "\t" . '{ ' . join(', ', @f2) . " }\n");
}