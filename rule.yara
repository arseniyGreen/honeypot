rule meterpreter{

	strings:
		$type = "POST"
		$page = "wp-login.php"
	condition:
		$type and $page
}
