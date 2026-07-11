%global tl_name pst-eucl-translation-bg
%global tl_revision 19296

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3.2
Release:	%{tl_revision}.1
Summary:	Bulgarian translation of the pst-eucl documentation
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/info/translations/pst-eucl/bulgarian
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eucl-translation-bg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/pst-eucl-translation-bg.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The pst-eucl package documentation in Bulgarian language - Euclidean
Geometry with PSTricks.

