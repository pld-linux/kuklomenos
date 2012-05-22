# TODO:
# - polish description and summary
# - desktop file and pixmap
Summary:	An abstract shoot-em-up with a strategical twist
Summary(pl.UTF-8):	Abstrakcyjna strzelanka.
Name:		kuklomenos
Version:	0.4.5
Release:	1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://mbays.freeshell.org/kuklomenos/src/%{name}-%{version}.tar.gz
# Source0-md5:	e88729b2385c5c60e708d7ebba918a42
URL:		http://mbays.freeshell.org/kuklomenos/
BuildRequires:	SDL-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_mixer-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An abstract shoot-em-up with a strategical twist. Minimalistic
graphics, short game-length. Very challenging at the higher difficulty
levels.

%description(pl.UTF-8):
Abstrakcyjna strzelanka z połączeniem strategii. Minimalistyczna
grafika i krótki czas gry. Bardzo wymagająca w wyższych poziomach
trudności.

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
%dir %{_datadir}/%{name}/fonts
%{_datadir}/%{name}/fonts/*.fnt
%dir %{_datadir}/%{name}/sounds
%{_datadir}/%{name}/sounds/*.ogg
