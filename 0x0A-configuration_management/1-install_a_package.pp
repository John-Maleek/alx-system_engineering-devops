# Installs a package using pip3

package { 'install_flask':
  name => 'flask'
  ensure => '2.1.0',
  provider => 'pip3',
}
