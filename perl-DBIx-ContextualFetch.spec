#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DBIx-ContextualFetch
Version  : 1.03
Release  : 28
URL      : https://cpan.metacpan.org/authors/id/T/TM/TMTM/DBIx-ContextualFetch-1.03.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/T/TM/TMTM/DBIx-ContextualFetch-1.03.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libd/libdbix-contextualfetch-perl/libdbix-contextualfetch-perl_1.03-4.debian.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-DBIx-ContextualFetch-license = %{version}-%{release}
Requires: perl-DBIx-ContextualFetch-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DBI)

%description
NAME
DBIx::ContextualFetch - Add contextual fetches to DBI
SYNOPSIS
my $dbh = DBI->connect(...., { RootClass => "DBIx::ContextualFetch" });

%package dev
Summary: dev components for the perl-DBIx-ContextualFetch package.
Group: Development
Provides: perl-DBIx-ContextualFetch-devel = %{version}-%{release}
Requires: perl-DBIx-ContextualFetch = %{version}-%{release}

%description dev
dev components for the perl-DBIx-ContextualFetch package.


%package license
Summary: license components for the perl-DBIx-ContextualFetch package.
Group: Default

%description license
license components for the perl-DBIx-ContextualFetch package.


%package perl
Summary: perl components for the perl-DBIx-ContextualFetch package.
Group: Default
Requires: perl-DBIx-ContextualFetch = %{version}-%{release}

%description perl
perl components for the perl-DBIx-ContextualFetch package.


%prep
%setup -q -n DBIx-ContextualFetch-1.03
cd %{_builddir}
tar xf %{_sourcedir}/libdbix-contextualfetch-perl_1.03-4.debian.tar.xz
cd %{_builddir}/DBIx-ContextualFetch-1.03
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/DBIx-ContextualFetch-1.03/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DBIx-ContextualFetch
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-DBIx-ContextualFetch/1ab94319440a93bc75813c4608968f8cb083268e
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DBIx::ContextualFetch.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DBIx-ContextualFetch/1ab94319440a93bc75813c4608968f8cb083268e

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
