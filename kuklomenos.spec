# TODO:
# - polish description and summary
# - desktop file and pixmap
Summary:	An abstract shoot-em-up with a strategical twist
Name:		kuklomenos
Version:	0.2.3.2
Release:	1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://mbays.freeshell.org/kuklomenos/src/%{name}-%{version}.tar.gz
# Source0-md5:	0cc4ec6d2b9819a2b434c8ebe0c685d3
URL:		http://mbays.freeshell.org/kuklomenos/
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An abstract shoot-em-up with a strategical twist. Minimalistic
graphics, short game-length. Very challenging at the higher difficulty
levels.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*.fnt
