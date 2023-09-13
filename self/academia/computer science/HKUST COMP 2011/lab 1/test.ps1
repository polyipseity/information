$program = "./lab1.exe"

for ($i = 1; Test-Path "./testcase/input${i}.txt"; ++$i) {
	Get-Content "./testcase/input${i}.txt" | & $program > "./testcase/output${i}.txt"
}
