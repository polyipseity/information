$inputPathPrefix = './input/input'
$newlines = "`r`n|[`n`v`f`r`u{85}`u{2028}`u{2029}]"
$outputPathPrefix = './output/output'
$program = './scu.exe'

function Normalize ([string]$text) {
	return ($text.Trim() -split $newlines | ForEach-Object { $_.Trim() }) -join "`n"
}

for ($i = 1;
	-not ((Test-Path "${inputPathPrefix}${i}.txt", "${outputPathPrefix}${i}.txt" -PathType Leaf) -ccontains $false);
	++$i) {
	$expected = Normalize (Get-Content "${outputPathPrefix}${i}.txt" -Raw)
	$output = Normalize ((Get-Content "${inputPathPrefix}${i}.txt" | & $program) -join "`n")
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
