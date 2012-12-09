# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fouridx
# catalog-date 2008-08-19 20:38:14 +0200
# catalog-license lppl
# catalog-version 1.00
Name:		texlive-fouridx
Version:	1.00
Release:	2
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.00-2
+ Revision: 752086
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.00-1
+ Revision: 718496
- texlive-fouridx
- texlive-fouridx
- texlive-fouridx
- texlive-fouridx

