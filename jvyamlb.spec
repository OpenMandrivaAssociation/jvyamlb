Name:           jvyamlb
Version:        0.1
Release:        %mkrel 0.2.1
Summary:        YAML processor for JRuby
Group:          Development/Libraries
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
