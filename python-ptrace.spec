%define module	ptrace
%define name	python-%{module}
%define version	0.4.1
%define release	%mkrel 1

Summary:        Python binding of the ptrace library
Name:		%{name}
Version: 	%{version}
Release: 	%{release}
Group: 		Development/Python
License:        GPLv2
URL:            http://python-ptrace.hachoir.org/trac/
Source:         http://pypi.python.org/packages/source/p/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}
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
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=FILELIST

%check
python ./test_doc.py 

%clean
%__rm -rf %{buildroot}

%files -f FILELIST
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
