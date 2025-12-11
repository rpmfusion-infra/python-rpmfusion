%global desc Python modules that help with building Fedora Services.  The client module\
included here can be used to build programs that communicate with many\
Fedora Infrastructure Applications such as Bodhi, PackageDB, MirrorManager,\
and FAS2.\


Name:           python-rpmfusion
Version:        1.2.2
Release:        2%{?dist}
BuildArch:      noarch

License:        LGPLv2+
Summary:        Python modules for talking to Fedora Infrastructure Services
URL:            https://github.com/rpmfusion-infra/python-rpmfusion
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gettext


%description
%{desc}

%package -n python3-rpmfusion
Summary:        %{summary}

Provides:       python3-fedora = %{version}-%{release}
Obsoletes:      python3-fedora < %{version}-%{release}

%{?python_provide:%python_provide python3-rpmfusion}


%description -n python3-rpmfusion
%{desc}


%prep
%autosetup -p1
%generate_buildrequires

%pyproject_buildrequires -p


%build
%pyproject_wheel


%install
%pyproject_install


%files -n python3-rpmfusion
%license COPYING
%{python3_sitelib}/fedora/
%{python3_sitelib}/python_rpmfusion*dist-info

%changelog
* Fri Jul 25 2025 Sérgio Basto <sergio@serjux.com> - 1.2.2-2
- Remove more unused translations

* Fri Jul 25 2025 Sérgio Basto <sergio@serjux.com> - 1.2.2-1
- Update python-rpmfusion to 1.2.2

* Fri May 23 2025 Sérgio Basto <sergio@serjux.com> - 1.2.1-1
- Update to 1.2.1

* Wed Mar 19 2025 Leigh Scott <leigh123linux@gmail.com> - 1.2-2
- rebuilt

* Wed Mar 19 2025 Sérgio Basto <sergio@serjux.com> - 1.2-1
- rpmfusion version

* Fri Jan 26 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Mon Jan 22 2024 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Sun Jul 02 2023 Python Maint <python-maint@redhat.com> - 1.1.1-9
- Rebuilt for Python 3.12

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Fri Jul 22 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Tue Jun 14 2022 Python Maint <python-maint@redhat.com> - 1.1.1-6
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Fri Jun 04 2021 Python Maint <python-maint@redhat.com> - 1.1.1-3
- Rebuilt for Python 3.10

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Thu Nov 26 2020 Aurelien Bompard <abompard@fedoraproject.org> - 1.1.1-1
- Version 1.1.1

* Thu Nov 19 2020 Kevin Fenzi <kevin@scrye.com> - 1.1.0-3
- Drop python2-fedora obsoletes, they are in fedora-obsolete-packages. Fixes bug #1898498

* Mon Nov 02 2020 Nils Philippsen <nils@redhat.com> - 1.1.0-2
- Obsolete python2-fedora (#1605204)

* Mon Nov 02 2020 Aurelien Bompard <abompard@fedoraproject.org> - 1.1.0-1
- Version 1.1.0

* Sun Sep 27 2020 Kevin Fenzi <kevin@scrye.com> - 1.0.0-1
- Update to 1.0.0. Fixes #1796367

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 25 2020 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-14
- Rebuilt for Python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 21 2020 Frantisek Zatloukal <fzatlouk@redhat.com> - 0.10.0-12
- Backport https://github.com/fedora-infra/python-fedora/commit/4719f10b3af1cf068e969387eab7df7e935003cd

* Tue Sep  3 2019 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 0.10.0-11
- Drop python2 subpackages: python2-fedora, python2-fedora-flask (#1748242)

* Sun Aug 18 2019 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-10
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Wed Oct 24 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-7
- Dropped python2-fedora-turbogears from Fedora (#1639859)

* Mon Oct 15 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-6
- Dropped python2-fedora-turbogears2 (#1634646)

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 0.10.0-4
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Feb 01 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.10.0-2
- Django is dead to me

* Thu Feb 01 2018 Patrick Uiterwijk <patrick@puiterwijk.org> - 0.10.0-1
- Rebase to upstream 0.10.0

* Mon Jan 22 2018 Lumír Balhar <lbalhar@redhat.com> - 0.9.0-8
- New upstream and source URLs

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jul 07 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.9.0-6
- Correct a few more requires to use python2- versions.

* Fri Jul 07 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.9.0-5
- Use python2- dependencies where available.

* Thu Jul 06 2017 Randy Barlow <bowlofeggs@fedoraproject.org> - 0.9.0-4
- Provide python2- subpackages.
- Use the license macro.

* Fri May 05 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.9.0-3
- Add python-openidc-client dependency

* Fri May 05 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.9.0-2
- In EL6 this is Django

* Fri May 05 2017 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.9.0-1
- Rebase to 0.9.0

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Adam Williamson <awilliam@redhat.com> - 0.8.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Apr 23 2016 Patrick Uiterwijk <puiterwijk@redhat.com> - 0.8.0-1
- Rebase to 0.8.0 release
- flask_fas was removed

* Thu Feb 18 2016 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.7.1-4
- Create a python3-fedora-flask subpackage
- Requires and Buildrequires updated from Django to python-django

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jan 11 2016 Ralph Bean <rbean@redhat.com> - 0.7.1-2
- Fix cherrypy BuildReq versioning for epel7.

* Mon Jan 11 2016 Ralph Bean <rbean@redhat.com> - 0.7.1-1
- new version

* Thu Jan 07 2016 Ralph Bean <rbean@redhat.com> - 0.7.0-1
- new version

* Mon Jan 04 2016 Ralph Bean <rbean@redhat.com> - 0.6.4-2
- Drop requirement on simplejson (RHBZ#1294543).

* Tue Dec 01 2015 Ralph Bean <rbean@redhat.com> - 0.6.4-1
- new version

* Wed Nov 18 2015 Adam Williamson <awilliam@redhat.com> - 0.6.2-7
- re-enable python3-fedora now python3-openid is rebuilt

* Mon Nov 16 2015 Ralph Bean <rbean@redhat.com> - 0.6.2-6
- Patch out python-lockfile dep at the setuptools level to avoid pbr breakage.
- Disable python3 subpackage while rawhide buildroot is broken.

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Oct 30 2015 Ralph Bean <rbean@redhat.com> - 0.6.2-4
- Adjust the python-requests version requirement for epel7.

* Fri Oct 23 2015 Ralph Bean <rbean@redhat.com> - 0.6.2-3
- Require a more modern python-requests since we dropped support for the
  older .json property.

* Tue Oct 20 2015 Ralph Bean <rbean@redhat.com> - 0.6.2-2
- Add dep on python3-lockfile.

* Tue Oct 13 2015 Ralph Bean <rbean@redhat.com> - 0.6.2-1
- Force the Bodhi2 url in the BodhiClient shim (for /usr/bin/bodhi).

* Mon Oct 12 2015 Ralph Bean <rbean@redhat.com> - 0.6.1-1
- Fix a bug in the BodhiClient where the Bodhi2Client would try to use the old
  Bodhi1 base url.
- Raise an AuthError if no username or password is provided to the openid login
  function.

* Fri Oct 09 2015 Ralph Bean <rbean@redhat.com> - 0.6.0-1
- Cache session cookies between use for clients using OpenID.
- Retry failed requests for clients using OpenID
- Remove Bodhi server version detection code.
- Python3 support for the BodhiClient.
- Drop support for python-requests-1.x
- Add dep on python-lockfile.

* Fri Sep 04 2015 Ralph Bean <rbean@redhat.com> - 0.5.6-1
- Python2.6 fix for el6.

* Thu Aug 27 2015 Ralph Bean <rbean@redhat.com> - 0.5.5-2
- Specbump for F21.  https://github.com/fedora-infra/bodhi/issues/363

* Wed Aug 19 2015 Ralph Bean <rbean@redhat.com> - 0.5.5-1
- Consistent exception handling in the Bodhi2Client.
- More adjustments to bodhi server version detection.

* Tue Aug 18 2015 Ralph Bean <rbean@redhat.com> - 0.5.4-1
- Adjust usage of python-six to be compatible with older versions on rhel7.
- More updates to detection of the bodhi server version.

* Tue Aug 18 2015 Ralph Bean <rbean@redhat.com> - 0.5.3-1
- Better compatibility with 'fedpkg update' for bodhi.

* Mon Aug 17 2015 Ralph Bean <rbean@redhat.com> - 0.5.2-1
- Better version checking against the bodhi server.

* Mon Aug 17 2015 Ralph Bean <rbean@redhat.com> - 0.5.1-1
- Typofix in the BodhiClient.

* Mon Aug 17 2015 Ralph Bean <rbean@redhat.com> - 0.5.0-1
- Bodhi2 compatibility.
- Return munch object from OpenIdBaseClient.
- Minor python3 fixes.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon May 04 2015 Ralph Bean <rbean@redhat.com> - 0.4.0-2
- More specific directory ownership for the core packages.

* Tue Apr 28 2015 Ralph Bean <rbean@redhat.com> - 0.4.0-1
- Upstream release.
- python3 subpackages.
- New deps on python-munch and python-six.

* Sat Jan 24 2015 Xavier Lamien <laxathom@fedoraproject.org> - 0.3.37-1
- Upstream release.

* Thu Oct 23 2014 Pierre-Yves Chibon <pingou@pingoured.fr> - 0.3.36-2
- Backport the flask-fas-openid fix merged upstream at:
  https://github.com/fedora-infra/python-fedora/pull/108

* Thu Aug  7 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.36-1
- New upstream release fixing logging in openidbaseclient

* Wed Aug  6 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.35-1
- Upstream 0.3.35 release that adds openidbaseclient

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May  2 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.34-1
- Upstream 0.3.34 release with security fixes for TG and flask services built
  with python-fedora

* Fri Mar 14 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.33-3
- Do not build the TG1 subpackage on EPEL7.  Infrastructure is going to port
  its applications away from TG1 by the time they switch to RHEL7.  So we want
  to get rid of TurboGears1 packages before RHEL7.
- Fix conditionals so that they include the proper packages on epel7

* Fri Jan 10 2014 Dennis Gilmore <dennis@ausil.us> - 0.3.33-2
- clean up some rhel logic in the spec

* Thu Dec 19 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.33-1
- Update for final release with numerous flask_fas_openid fixes

* Mon Jul 29 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.32.3-3
- Update flask_fas_openid to fix imports

* Tue Jul 23 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.32.3-2
- Add the flask_fas_openid identity provider for flask

* Tue Feb  5 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.32.3-1
- Upstream update to fix BodhiClient's knowledge of koji tags (ajax)

* Mon Feb 04 2013 Toshio Kuratomi <toshio@fedoraproject.org> 0.3.32.2-1
- Upstream update fixing a bug interacting with python-requests

* Thu Jan 24 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.32.1-1
- Fix a documentation bug that slipped through

* Wed Jan 23 2013 Ralph Bean <rbean@redhat.com> - 0.3.32-1
- Replace pyCurl with python-requests in ProxyClient.

* Tue Jan 22 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.31-1
- Minor bugfix release

* Thu Jan 10 2013 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.30-1
- Make TG's loginForm and CSRF's text translated from tg-apps (laxathom).
- Fix a bug in fedora.tg.utils.tg_absolute_url
- Add a lookup email parameter to gravatar lookups
- Add an auth provider for flask

* Wed Jun 6 2012 Ricky Elrd <codeblock@fedoraproject.org> - 0.3.29-1
- Add a create_group() method to AccountSystem.

* Tue Apr 17 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.28.1-1
- Apply the apache-curl workaround unconditionally, not just when doing
  authenticated requests

* Tue Apr 17 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.28-1
- Bugfix for a bad interaction between curl and the apache version running on
  Fedora Infrastructure leading to Http 417 errors.
- Bugfix for older Django installations.

* Thu Mar 8 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.27-1
- Bugfix release for servers using tg-1.1.x

* Mon Feb 13 2012 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.26-1
- Final release.

* Thu Dec 22 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.25.92-1
- Third beta release

* Sun Nov 20 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.25.90-1
- Beta release

* Thu Oct 6 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.25.1-1
- Minor update to bugzilla email aliases

* Sat Sep 3 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.25-1
- Upstream bugfix release that makes many TG2-server helper function more usable
- Also, split the TG2 functionality into a separate subpackage from the TG1
  functions

* Tue Aug 9 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.24-3
- Get the PYTHONPATH for building docs correct

* Tue Aug 9 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.24-2
- Rework package to provide the turbogears and django code in subpackages with
  full dependencies for each of those.

* Wed Jul 20 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.24-1
- Upstream 0.3.24 release bugfixing TG2 server utils and clients with
  session cookie auth.

* Tue May 03 2011 Luke Macken <lmacken@redhat.com> - 0.3.23-1
- Upstream 0.3.23 bugfix release

* Fri Apr 29 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.22-1
- Upstream 0.3.22 bugfix release

* Mon Apr 11 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.21-1
- Upstream 0.3.21 release

* Mon Feb 28 2011 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.21-0.a1
- 0.3.21 alpha1 release.

* Thu Apr 22 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.20-1
- 0.3.20 release

* Wed Apr 21 2010 Luke Macken <lmacken@redhat.com> - 0.3.19-1
- 0.3.19 release

* Mon Mar 15 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.18.90-1
- 0.3.18.90: beta of a bugfix release

* Mon Mar 15 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.18-1
- 0.3.18 bugfix.

* Thu Mar 11 2010 Toshio Kuratomi <toshio@fedoraproject.org> - 0.3.17-1
- New release 0.3.17.
