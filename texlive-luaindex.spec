# revision 25882
# category Package
# catalog-ctan /macros/luatex/latex/luaindex
# catalog-date 2011-08-19 10:28:18 +0200
# catalog-license lppl1.3
# catalog-version 0.1b
Name:		texlive-luaindex
Version:	0.1b
Release:	12
Summary:	Create index using lualatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luaindex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Luaindex provides (yet another) index processor, written in
Lua.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/luaindex/luaindex.lua
%{_texmfdistdir}/tex/lualatex/luaindex/luaindex.sty
%doc %{_texmfdistdir}/doc/lualatex/luaindex/README
%doc %{_texmfdistdir}/doc/lualatex/luaindex/luaindex-example.ldx
%doc %{_texmfdistdir}/doc/lualatex/luaindex/luaindex-example.ltx
%doc %{_texmfdistdir}/doc/lualatex/luaindex/luaindex-example.pdf
%doc %{_texmfdistdir}/doc/lualatex/luaindex/luaindex.ltx
%doc %{_texmfdistdir}/doc/lualatex/luaindex/luaindex.pdf
#- source
%doc %{_texmfdistdir}/source/lualatex/luaindex/luaindex.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Fri Apr 13 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1b-3
+ Revision: 790649
- Update to latest release.

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1b-2
+ Revision: 753582
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1b-1
+ Revision: 718921
- texlive-luaindex
- texlive-luaindex
- texlive-luaindex
- texlive-luaindex

