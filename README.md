# PHP-FILE
Certainly! Here's an example of a basic PHP web server that says "Hello, World!":

```php
<?php
    echo "Hello, World!";
?>
```

To create a Docker container for this PHP web server, follow these steps:

1. Create a directory for your project and navigate to it.
```
mkdir my-php-webserver
cd my-php-webserver
```

2. Create a file named `index.php` in the project directory and add the following content to it:
```php
<?php
    echo "Hello, World!";
?>
```

3. Create a file named `Dockerfile` (without any file extension) in the same directory and add the following content to it:
```
FROM php:7.4-apache
COPY index.php /var/www/html/
EXPOSE 80
```

4. Save the `Dockerfile`.

5. Open a terminal or command prompt, navigate to the project directory.

6. Build the Docker image using the following command:
```
docker build -t my-php-webserver .
```
This command will build the Docker image based on the instructions in the `Dockerfile` and tag it with the name `my-php-webserver`.

7. Once the image is built, you can run a Docker container using the following command:
```
docker run -p 80:80 my-php-webserver
```
This command maps port 80 from the Docker container to port 80 on your EC2 instance, so you can access the web server using your EC2 instance's public IP address.

Make sure to replace `my-php-webserver` with your desired image name.

Now you have a Docker container running the PHP web server. You can access it by visiting your EC2 instance's public IP address in a web browser, and you should see "Hello, World!" displayed.

Please note that you need to have Docker installed and properly configured on your EC2 instance to run the Docker container.
