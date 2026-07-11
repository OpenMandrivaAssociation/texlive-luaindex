%global tl_name luaindex
%global tl_revision 25882

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1b
Release:	%{tl_revision}.1
Summary:	Create index using LuaLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/luatex/latex/luaindex
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/luaindex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Luaindex provides (yet another) index processor, written in Lua.

