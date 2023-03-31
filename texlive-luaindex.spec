Name:		texlive-luaindex
Version:	25882
Release:	2
Summary:	Create index using lualatex
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/luatex/latex/luaindex
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc source %{buildroot}%{_texmfdistdir}
