$inputNamePrefix = 'input'
$newlines = "`r`n|[`n`v`f`r`u{85}`u{2028}`u{2029}]"
$outputNamePrefix = 'output'
$program = './lab3.exe'
$testFolder = './testcase'

function Normalize ([string]$text) {
	return ($text.Trim() -split $newlines | ForEach-Object { $_.Trim() }) -join "`n"
}

for ($i = 1;
	-not ((Test-Path "${testFolder}/${inputNamePrefix}${i}.txt", "${testFolder}/${outputNamePrefix}${i}.txt" -PathType Leaf) -ccontains $false);
	++$i) {
	$expected = Normalize (Get-Content "${testFolder}/${outputNamePrefix}${i}.txt" -Raw)
	$output = Normalize ((Get-Content "${testFolder}/${inputNamePrefix}${i}.txt" | & $program) -join "`n")
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
