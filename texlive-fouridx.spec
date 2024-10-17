Name:		texlive-fouridx
Version:	32214
Release:	2
Summary:	Left sub- and superscripts in maths mode
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fouridx
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fouridx.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fouridx.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fouridx.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
