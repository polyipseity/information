for ($i = 1; $i -le 3; ++$i) {
	Get-Content "testcase/input${i}.txt" | ./lab1.exe > "testcase/output${i}.txt"
}
