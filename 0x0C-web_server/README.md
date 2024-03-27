Configuring the Web server

0-transfer_file

1. My public key is saved in the path ~/.ssh/school
2. To login into my server i run the [ssh -i ~/.ssh/school ubuntu@54.161.240.95] command 
3. Run the script ./0-transfer_file Test.txt 54.161.240.95 ubuntu ~/.ssh/school to transfer the file Text.txt from client to server

404-not-found-page
1.Run command with system priviledges sudo ./404-not_found_page_404

Install Nginx web server (w/ Puppet)
1. Run puppet as sudo puppet apply 7-puppet_install_nginx_web_server.pp
