$program = "./lab1.exe"

for ($i = 1;
	-not ((Test-Path "./testcase/input${i}.txt", "./testcase/output${i}.txt" -PathType Leaf) -contains $false);
	++$i) {
	$output = Get-Content "./testcase/input${i}.txt" | & $program
	if ($output -eq (Get-Content "./testcase/output${i}.txt")) {
		Write-Output "Test ${i} succeeded"
	}
	else {
		Write-Output "=======Test ${i} failed======="
		Write-Output $output
		Write-Output '=============================='
	}
}
