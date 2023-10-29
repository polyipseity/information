$program = './pa2.exe'

for ($i = 1;
	-not ((Test-Path "./tests/input${i}.txt", "./tests/output${i}.txt" -PathType Leaf) -ccontains $false);
	++$i) {
	$output = ((Get-Content "./tests/input${i}.txt" | & $program) -join "`n").Trim() -split "`r`n|[`n`v`f`r`u{85}`u{2028}`u{2029}]" -join "`n"
	if ($output -ceq ((Get-Content "./tests/output${i}.txt" -Raw).Trim() -split "`r`n|[`n`v`f`r`u{85}`u{2028}`u{2029}]" -join "`n")) {
		Write-Output "Test ${i} succeeded"
	}
	else {
		$header = "=======Test ${i} failed======="
		Write-Output $header
		Write-Output $output
		Write-Output ('=' * $header.Length)
	}
}
