# About

A *simple* one line command to build a node.js RPM. 

## Usage and Example Output

    > ./create-node-rpm.sh 0.10.21
    2013 11 05 12:01:20 Fetching http://nodejs.org/dist/v0.10.21/node-v0.10.21.tar.gz
    2013 11 05 12:01:39 Download OK. SHA1 sums match: b7fd2a3660635af40e3719ca0db49280d10359b2
    2013 11 05 12:01:39 Building SRPM
    2013 11 05 12:01:55 Building Node.js RPM

## Prerequisites 

* [mock](http://fedoraproject.org/wiki/Projects/Mock) - builds RPM packages in a chroot
* RHEL/SL/Centos 6.3+

## Details

The `spec/` contains spec files for building specific versions of nodejs. These 
are used to generated an SRPM package (also using mock). Then the SRPM is used 
to build a node.js binary RPM. 

Output goes into the `./BUILD` sub-directory (automatically created if missing). 
Once a build has completed, simply put the RPM in `./BUILD/RPMS/` into the appropriate
repo for usage. 
