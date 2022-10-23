%define module	ptrace

Summary:        Python binding of the ptrace library

Name:		python-%{module}
Version: 	1.0.1
Release: 	1
Group: 		Development/Python
License:        GPLv2
URL:            https://pypi.org/project/ptrace
Source:         https://files.pythonhosted.org/packages/source/p/ptrace/ptrace-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:	python-devel

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
%autosetup -p1 -n ptrace-%{version}
find . -name "*.py" |xargs 2to3 -w

%build
%py_build

%install
%py_install

%check
python ./test_doc.py

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/*
%{py_puresitedir}/*
