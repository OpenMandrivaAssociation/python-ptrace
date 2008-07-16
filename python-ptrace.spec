%define module	ptrace
%define name	python-%{module}
%define version	0.3.1
%define release	%mkrel 1

Name:		%{name}
Version: 	%{version}
Release: 	%{release}
Summary:        Python bindings of ptrace syscall
Group: 		Development/Python
License:        GPL v2
URL:            http://fusil.hachoir.org/trac/wiki/Ptrace
Source:         http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      noarch
BuildRequires:	python-devel >= 2.2

%description
ptrace is a Python binding of ptrace library.
Features:

    * High level Python object API : PtraceDebugger and PtraceProcess
    * Able to control multiple processes: catch fork events on Linux
    * Read/write bytes to arbitrary address: take care of memory alignment and split bytes to cpu word
    * Execution step by step using ptrace_singlestep() or hardware interruption 3
    * Can use distorm disassembler
    * Dump registers, memory mappings, stack, etc.
    * Syscall tracer and parser (strace command) 

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%check
python ./test_doc.py 

%clean
rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc doc/* 
