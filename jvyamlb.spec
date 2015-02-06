Name:           jvyamlb
Version:        0.2.5
Release:        2
Summary:        YAML processor for JRuby
Group:          Development/Java
License:        MIT
URL:            http://code.google.com/p/jvyamlb/
Source0:        http://jvyamlb.googlecode.com/files/%{name}-src-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  ant-junit
BuildRequires:  bytelist
BuildRequires:  java-rpmbuild >= 1.5
BuildRequires:  joda-time
BuildRequires:  jpackage-utils
BuildRequires:  junit

Requires:       bytelist
Requires:       java >= 1.5
Requires:       joda-time
Requires:       jpackage-utils

%description
YAML processor extracted from JRuby.

%prep
%setup -q
rm lib/*
build-jar-repository -s -p lib joda-time bytelist

%build
%ant

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_javadir}
cp -p lib/%{name}-%{version}.jar \
       $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

%check
%ant test

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_javadir}/%{name}.jar
%doc LICENSE README CREDITS


%changelog
* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 0.2.5-1mdv2011.0
+ Revision: 645248
- update to new version 0.2.5

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2.2-0.0.3mdv2011.0
+ Revision: 619873
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.2.2-0.0.2mdv2010.0
+ Revision: 429654
- rebuild

* Thu Aug 14 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0.2.2-0.0.1mdv2009.0
+ Revision: 271822
- new version 0.2.2

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.1.4-2.0.1mdv2009.0
+ Revision: 267343
- rebuild early 2009.0 package (before pixel changes)

* Wed May 28 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0.1.4-0.0.1mdv2009.0
+ Revision: 212539
- new version

* Mon Apr 28 2008 Alexander Kurtakov <akurtakov@mandriva.org> 0.1-0.2.1mdv2009.0
+ Revision: 198715
- fix group
- import jvyamlb


