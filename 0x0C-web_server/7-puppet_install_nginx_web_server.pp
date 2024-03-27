#!/usr/bin/env bash
# Install NginX
# With puppet

# Update package lists
exec { 'apt-get-update':
  command => '/usr/bin/apt-get update',
}

# Install Nginx package
package { 'nginx':
  ensure  => installed,
  require => Exec['apt-get-update'],
}

# Create index.html file
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

# Ensure Nginx service is running and restart when configuration changes
service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
