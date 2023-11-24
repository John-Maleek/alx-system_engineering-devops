# Installs a package using pip3

package { 'install_flask':
  name => 'flask',
  ensure => installed,
  provider => 'pip3',
  version => '2.1.0'
}
