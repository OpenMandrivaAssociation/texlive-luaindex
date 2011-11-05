# revision 23577
# category Package
# catalog-ctan /macros/luatex/latex/luaindex
# catalog-date 2011-02-21 15:41:42 +0100
# catalog-license lppl1.3
# catalog-version 0.1b
Name:		texlive-luaindex
Version:	0.1b
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
Luaindex provides (yet another) index processor, written in
Lua.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
