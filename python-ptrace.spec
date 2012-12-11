%define module	ptrace
%define name	python-%{module}
%define version	0.6.2
%define release	2

Summary:        Python binding of the ptrace library
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		Development/Python
License:        GPLv2
URL:            http://python-ptrace.hachoir.org/trac/
Source:         http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	python-devel >= 2.4

%description
python-ptrace is a Python binding of the ptrace library with the
following features:

* High level Python object API: PtraceDebugger and PtraceProcess
* Ability to control multiple processes; can catch fork events on Linux
* Can read/write bytes to arbitrary address; takes care of memory alignment
  and split bytes to cpu word
* Step-by-step execution using ptrace_singlestep() or hardware interruption 3
* Can use distorm disassembler
* Can dump registers, memory mappings, stack, etc.
* Provides system call tracer and parser (strace command)

%prep
%setup -q -n %{name}-%{version}

%build
%__python setup.py build

%install
%__python setup.py install --root=%{buildroot} --record=FILELIST

%check
python ./test_doc.py

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%py_puresitedir/*


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 0.6.2-1mdv2011.0
+ Revision: 598278
- rebuild for py2.7

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.2-1mdv2010.1
+ Revision: 489189
- update to new version 0.6.2

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 0.6-2mdv2010.0
+ Revision: 442403
- rebuild

* Fri Feb 13 2009 Michael Scherer <misc@mandriva.org> 0.6-1mdv2009.1
+ Revision: 340063
- update to new version 0.6

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.5-2mdv2009.1
+ Revision: 323929
- rebuild

* Sat Sep 13 2008 Michael Scherer <misc@mandriva.org> 0.5-1mdv2009.0
+ Revision: 284485
- update to new version 0.5

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.4.2-1mdv2009.0
+ Revision: 280561
- New version

* Mon Aug 25 2008 Lev Givon <lev@mandriva.org> 0.4.1-1mdv2009.0
+ Revision: 275906
- Update to 0.4.1.

* Mon Jul 28 2008 Michael Scherer <misc@mandriva.org> 0.3.2-1mdv2009.0
+ Revision: 251265
- update to new version 0.3.2

* Wed Jul 16 2008 Michael Scherer <misc@mandriva.org> 0.3.1-1mdv2009.0
+ Revision: 236562
- import python-ptrace


