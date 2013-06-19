About
-----

This outputs `.spec` that can be used to build SRPM files which can later be passed to [mock](http://fedoraproject.org/wiki/Projects/Mock).

Usage
-----

`./create-srpm $NODE_VERSION

This will build the SRPM file into `./srpms/`. To turn it into an RPM use: 

`mock --rebuild ./srpms/nodejs-0.8.19-1.el6.src.rpm`
