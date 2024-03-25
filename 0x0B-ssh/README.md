SSH and server
I created a ssh key using ssh-keygen and defined my path to /root/.ssh/school
- This will direct the generated ssh key into the defined path
I got two files in the defined path as school as private key and school.pub as public key
I copied my school.pub key to alx intranet
I made school executable by defining chmod 600
I reran my server after makng this changes
ssh -i ~/.ssh/school ubuntu@<ip.address>
I got authenticated into the running server at [ubuntu@492852-web-01]
Then i copied the key provided in the task to ~/.ssh/authorized_key in the running server
I exited and ran the checker
