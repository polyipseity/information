$inputNameFormat = 'input{0:d2}.txt'
$newlines = "`r`n|[`n`v`f`r`u{85}`u{2028}`u{2029}]"
$outputNameFormat = 'output{0:d2}.txt'
$program = './pa3.exe'
$testFolder = './testcase'

function Normalize ([string]$text) {
	return ($text.Trim() -split $newlines | ForEach-Object { $_.Trim() }) -join "`n"
}

for ($i = 1;
	-not ((Test-Path "${testFolder}/$($inputNameFormat -f $i)", "${testFolder}/$($outputNameFormat -f $i)" -PathType Leaf) -ccontains $false);
	++$i) {
	$expected = Normalize (Get-Content "${testFolder}/$($outputNameFormat -f $i)" -Raw)
	$output = Normalize ((Get-Content "${testFolder}/$($inputNameFormat -f $i)" | & $program) -join "`n")
	if ($output -ceq $expected) {
		Write-Output "Test ${i} succeeded"
	}
	else {
		$header = "=======Test ${i} failed======="
		Write-Output $header
		Write-Output $output
		Write-Output ('=' * $header.Length)
	}
}
