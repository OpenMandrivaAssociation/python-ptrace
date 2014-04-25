%define module	ptrace

Summary:        Python binding of the ptrace library

Name:		python-%{module}
Version: 	0.7
Release: 	1
Group: 		Development/Python
License:        GPLv2
URL:            http://python-ptrace.hachoir.org/trac/
Source:         http://pypi.python.org/packages/source/p/python-ptrace/%{name}-%{version}.tar.gz
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
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{py_puresitedir}/*



