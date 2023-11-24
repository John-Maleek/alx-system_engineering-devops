# Kills a process using Puppet

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow'
}
