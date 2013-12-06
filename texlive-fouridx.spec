# revision 32214
# category Package
# catalog-ctan /macros/latex/contrib/fouridx
# catalog-date 2013-11-21 22:41:55 +0100
# catalog-license lppl
# catalog-version 2.00
Name:		texlive-fouridx
Version:	2.00
Release:	3
Summary:	Left sub- and superscripts in maths mode
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fouridx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fouridx.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fouridx.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fouridx.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package enables left subscripts and superscripts in maths
mode. The sub- and superscripts are raised for optimum fitting
to the symbol indexed, in such a way that left and right sub-
and superscripts are set on the same level, as appropriate. The
package provides an alternative to the use of the \sideset
command in the amsmath package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fouridx/fouridx.sty
%doc %{_texmfdistdir}/doc/latex/fouridx/README
%doc %{_texmfdistdir}/doc/latex/fouridx/fouridx.pdf
#- source
%doc %{_texmfdistdir}/source/latex/fouridx/fouridx.dtx
%doc %{_texmfdistdir}/source/latex/fouridx/fouridx.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
