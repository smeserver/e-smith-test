Summary: e-smith server and gateway - testing infrastructure module
%define name e-smith-test
Name: %{name}
%define version 1.2.0
%define release 2
Version: %{version}
Release: %{release}%{?dist}
License: Artistic
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
BuildArchitectures: noarch
Requires: perl
Requires: perl(WWW::Automate) >= 0.20
Requires: perl(Test::Simple) >= 0.41
Requires: perl(Test::Inline) >= 0.14
Requires: perl(Test::Harness::Straps) >= 0.10
Requires: e-smith-lib >= 1.9.35
BuildRequires: e-smith-devtools >= 1.7.1

%description
e-smith server and gateway software - testing infrastructure module.

%changelog
* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Thu Mar 16 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-01
- Roll stable stream version. [SME: 1016]

* Wed Nov 30 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-07
- Bump release number only

* Thu Sep 22 2005 Trevor Poole <trevorp@e-smith.com>
- [1.0.1-06]
- Rollback change to smoketest

* Thu Sep 22 2005 Trevor Poole <trevorp@e-smith.com>
- [1.0.1-05]
- Add a sort to the test names in smoketest 

* Fri Aug 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.1-04]
- Actually remove AutoReqProv header (see 1.0.1-02)

* Tue Aug  2 2005 Shad Lords <slords@email.com>
- [1.0.1-03]
- Update for move of default database location. [SF: 1216546]

* Sun Sep 19 2004 Charlie Brady <charlieb@e-smith.com>
- [1.0.1-02]
- Change deprecated "Copyright:" header to "License:".
- Updated requires with new perl dependencies. [charlieb MN00040240]
- Remove "AutoReqProv: no" so that "Provides" headers are auto-generated.
  [charlieb MN00040240]

* Wed Sep  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.0.1-01]
- Rebuild [gordonr 1305]

* Wed Sep  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.0.0-04]
- Revert unwanted code change in END block [gordonr 1305]

* Wed Sep  3 2003 Gordon Rowell <gordonr@e-smith.com>
- [1.0.0-03]
- Copyright update [gordonr 1305]

* Mon Feb 24 2003 Michael Soulier <msoulier@e-smith.com>
- [1.0.0-02]
- Remove deprecated WebServerName setting from canned test data. [charlieb 6861]
- Removed any references to LocalDomainPrefix. [msoulier 4812]

- [1.0.0-01]
- Roll to maintained version number to 1.0.0

* Wed Jun  5 2002 Charlie Brady <charlieb@e-smith.com>
- [0.3.0-01]
- Changing version to maintained stream number to 0.3.0

* Mon Jun  3 2002 Charlie Brady <charlieb@e-smith.com>
- [0.2.0-01]
- Changing version to maintained stream number to 0.2.0

* Thu May 23 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.23-01]
- RPM rebuild forced by cvsroot2rpm

* Thu May  9 2002 Michael Schwern <schwern@e-smith.com>
- [0.1.22-01]
- Updating necessary Test::Harness::Straps version to 0.10
  [schwern 3408]

* Mon May  6 2002 Michael Schwern <schwern@e-smith.com>
- [0.1.21-01]
- Fixed quicktest to use an absolute path to the CVS lib directory.
  Helpful or tests which chdir. [schwern 2743]

* Thu May  2 2002 Michael Schwern <schwern@e-smith.com>
- [0.1.20-01]
- Fixed quicktest wrt files with spaces in the name [schwern]

* Wed May  1 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.19-01]
- esmith::AccountDB -> esmith::AccountsDB [schwern 3287]

* Wed Apr 24 2002 Michael Schwern <schwern@e-smith.com>
- [0.1.18-01]
- quicktest now propagates the new libraris into any perl programs
  called in the tests [schwern]

* Wed Apr 10 2002 Michael Schwern <schwern@e-smith.com>
- [0.1.17-01]
- Added a --verbose switch to quicktest [schwern]
- quicktest now running tests with warnings on [schwern]

* Sat Apr  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.16-01]
- Rebuild with new e-smith-devtools to force permissions [gordonr]

* Sat Apr  6 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.15-01]
- Added execute permission for all for {quick,smoke}test [gordonr]

* Fri Apr  5 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.14-01]
- Added -d option to quicktest for debugging [schwern]
- Added scratch_copy() to esmith::TestUtils [schwern]

* Fri Apr 05 2002 Gordon Rowell <gordonr@e-smith.com>
- [0.1.13-01]
- Run testing-conf in post-{install,upgrade} events rather than from %post
  Running it from %post won't work in a fresh install as the config 
  database doesn't yet exist [gordonr]

* Tue Apr 02 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.12-01]
- Added simulate_perl_program() to TestUtils [schwern]

* Mon Apr 01 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.11-01]
- Added destruction_ok() routine to TestUtils.pm [skud]

* Fri Mar 15 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.10-01]
- quicktest now closes STDIN so tests don't block waiting for it (3042)
- Fixed bug in Test::Harness::Straps so tests that die are failures (3034)

* Wed Mar 13 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.9-01]
- Added files argument to quicktest [schwern]
- 0.1.8-01 was tagged badly.  esmith::TestUtils was accidentally dropped
  and the temporary quiktest was accidentally installed [schwern 3026]
- Adding dependeny on e-smith-lib for esmith::ConfigDB in testing-conf
  [schwern]

* Mon Mar 11 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.8-01]
- Added quicktest [schwern]
- Added dependency on perl-Test-Harness-Straps [schwern]

* Thu Feb 28 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.7-01]
- General cleanup in esmith::TestUtils
- moved dependency on e-smith-devtools from Requires to BuildRequires [skud]

* Wed Feb 27 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.6-01]
- Botched the tagging again

* Wed Feb 27 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.5-01]
- Added dependency on e-smith-devtools for genfilelist update
- smoketest now looks for local Perl libraries
- fixed the sanity test

* Wed Feb 27 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.4-01]
- Botched the roll of 0.1.3-01

* Wed Feb 27 2002 Michael G Schwern <schwern@e-smith.com>
- [0.1.3-01]
- Fixed dependency on perl-Test-Simple [schwern]

* Mon Feb 18 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.2-01]
- Added an esmith::TestUtils perl module to assist in writing tests
- Changes to the smoketest script; now accepts an optional directory to
  run tests from, among other (internal) changes

* Mon Feb 18 2002 Kirrily Robert <skud@e-smith.com>
- [0.1.1-01]
- rollRPM: Rolled version number to 0.1.1-01. Includes patches up to 0.1.0-02.

* Sun Oct 07 2001 Kirrily Robert <skud@e-smith.com>
- Minor change to 00sanity.t as it didn't seem to like using Inline

* Sun Oct 07 2001 Kirrily Robert <skud@e-smith.com>
- Initial build

%prep
%setup

%pre

%post

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f e-smith-%{version}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT > e-smith-%{version}-filelist
echo "%doc Copying" >> %{name}-%{version}-%{release}-filelist
echo "%doc Artistic" >> %{name}-%{version}-%{release}-filelist
echo "%doc LICENSE" >> %{name}-%{version}-%{release}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%files -f e-smith-%{version}-filelist
%defattr(-,root,root)
