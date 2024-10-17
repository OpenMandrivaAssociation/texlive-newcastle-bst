Name:		texlive-newcastle-bst
Version:	62856
Release:	2
Summary:	A BibTeX style to format reference lists in the Harvard at Newcastle style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/newcastle-bst
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcastle-bst.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newcastle-bst.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides a BibTeX style to format reference lists
in the Harvard at Newcastle style recommended by Newcastle
University. It should be used alongside natbib for citations.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/bibtex/bst/newcastle-bst
%doc %{_texmfdistdir}/doc/bibtex/newcastle-bst

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
