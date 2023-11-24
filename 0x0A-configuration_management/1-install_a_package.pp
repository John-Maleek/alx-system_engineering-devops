# Installs a package using pip3

package { 'flask':
  ensure   => installed,
  version  => '2.1.0'
  provider => 'pip3',
}
