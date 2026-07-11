%global tl_name newcastle-bst
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	A BibTeX style to format reference lists in the Harvard at Newcastle style
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/biblio/bibtex/contrib/newcastle-bst
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newcastle-bst.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/newcastle-bst.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides a BibTeX style to format reference lists in the
Harvard at Newcastle style recommended by Newcastle University. It
should be used alongside natbib for citations.

