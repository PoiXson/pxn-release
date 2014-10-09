Name            : pxnExtrasRepo
Summary         : Installs the PoiXson yum repository
Version         : 1.0.%{BUILD_NUMBER}
Release         : 1
BuildArch       : noarch
Provides        : pxnyum
Prefix          : %{_sysconfdir}/yum.repos.d
%define  _rpmfilename  %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm

Group		: System Environment/Base
License		: GPL
URL             : http://yum.poixson.com/

%description
Installs the PoiXson yum repository.



# avoid centos 5/6 extras processes on contents (especially brp-java-repack-jars)
%define __os_install_post %{nil}

# disable debug info
# % define debug_package %{nil}



### Prep ###
%prep



### Build ###
%build
# build repo file
%{__cat} <<EOF >pxn.repo

[pxn-extras-noarch]
name=PoiXson Yum Extras
baseurl=http://yum.poixson.com/extras/noarch/
enabled=1
gpgcheck=0
priority=1

[pxn-extras]
name=PoiXson Yum Extras
baseurl=http://yum.poixson.com/extras/\$basearch/
enabled=1
gpgcheck=0
priority=1

EOF



### Install ###
%install
echo
echo "Install.."
# delete existing rpm's
%{__rm} -fv "%{_rpmdir}/%{name}-"*.noarch.rpm
# create directories
%{__install} -d -m 0755 \
	"${RPM_BUILD_ROOT}%{prefix}" \
		|| exit 1
# copy .repo file
%{__install} -m 0644 \
	"pxn.repo" \
	"${RPM_BUILD_ROOT}%{prefix}/pxn.repo" \
		|| exit 1



%check



%clean
if [ ! -z "%{_topdir}" ]; then
	%{__rm} -rf --preserve-root "%{_topdir}" \
		|| echo "Failed to delete build root!"
fi



### Files ###
%files
%defattr(644,-,-,755)
%{prefix}/pxn.repo

