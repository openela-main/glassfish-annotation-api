%global namedreltag %{nil}
%global namedversion %{version}%{?namedreltag}
%global oname javax.annotation-api
%global sname javax.annotation

Name:          glassfish-annotation-api
Version:       1.3.2
Release:       3%{?dist}
Summary:       Common Annotations API Specification (JSR 250)
License:       CDDL-1.1 or GPLv2 with exceptions

# NOTE: The new upstream repository under the Eclipse EE4J umbrella is here:
# https://github.com/eclipse-ee4j/common-annotations-api
# However, the new package provides a different groupId:artifactId.
URL:           https://github.com/javaee/%{sname}
Source0:       %{url}/archive/%{version}/%{sname}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(net.java:jvnet-parent:pom:)
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-remote-resources-plugin)
BuildRequires: mvn(org.apache.maven.plugins:maven-source-plugin)
BuildRequires: mvn(org.glassfish.build:spec-version-maven-plugin)
# xmvn-builddep misses this one
BuildRequires: mvn(org.glassfish:legal)

BuildArch:     noarch

%description
Common Annotations APIs for the Java Platform (JSR 250).

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -q -n %{sname}-%{namedversion}

%pom_remove_plugin :findbugs-maven-plugin
%pom_remove_plugin :maven-gpg-plugin
%pom_remove_plugin :maven-javadoc-plugin

%mvn_file :%{oname} %{name}

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%license LICENSE

%files javadoc -f .mfiles-javadoc
%license LICENSE

%changelog
* Wed Apr 01 2020 Mat Booth <mat.booth@redhat.com> - 1.3.2-3
- Avoid explicit javadoc plugin invokation

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 16 2019 Fabio Valentini <decathorpe@gmail.com> - 1.3.2-1
- Update to version 1.3.2.

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb 03 2015 gil cattaneo <puntogil@libero.it> 1.2-8
- introduce license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.2-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jul 08 2013 gil cattaneo <puntogil@libero.it> 1.2-4
- switch to XMvn
- minor changes to adapt to current guideline

* Sun May 26 2013 gil cattaneo <puntogil@libero.it> 1.2-3
- rebuilt with spec-version-maven-plugin support

* Wed May 22 2013 gil cattaneo <puntogil@libero.it> 1.2-2
- fixed manifest

* Tue May 07 2013 gil cattaneo <puntogil@libero.it> 1.2-1
- update to 1.2

* Tue Apr 02 2013 gil cattaneo <puntogil@libero.it> 1.2-0.1.b04
- initial rpm
