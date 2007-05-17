%define name	scribes
%define version 0.3.2.5
%define release %mkrel 1

Summary:	Simple yet powerful GNOME text editor
Name:		%name
Version:	%version
Release:	%release
License:	GPL 
Group:		Editors
URL:		http://scribes.sourceforge.net
Source0:	http://internap.dl.sourceforge.net/sourceforge/scribes/%name-%version.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
Buildrequires:	pygtk2.0-devel yelp dbus-python gnome-python gnome-python-extras gnome-python-gtkspell gnome-python-gtksourceview desktop-file-utils
Requires:	yelp dbus-python pygtk2.0 gnome-python gnome-python-extras gnome-python-gtkspell

%description
Scribes is a text editor for GNOME that is simple,
slim and sleek, yet powerful.

Scribes focuses on streamlining your workflow. 
It does so by ensuring common and repetitive operations 
are intelligently automated. And also by eliminating 
factors that prevent you from focusing on your tasks.

%prep
%setup -q

%build
%configure --disable-scrollkeeper --disable-schemas-install
%make

%install
%makeinstall_std
desktop-file-install --vendor="" \
  --add-category="Editors" \
  --add-category="X-MandrivaLinux-MoreApplications-Editors" \
  --add-category="X-MandrivaLinux-MoreApplications-Development" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang %name 

%post
%define schemas %name
%post_install_gconf_schemas %schemas
%update_scrollkeeper
%update_icon_cache hicolor
%update_desktop_database 

%preun
%preun_uninstall_gconf_schemas %schemas

%postun
%clean_scrollkeeper
%clean_icon_cache hicolor 
%clean_desktop_database

%clean
rm -rf %buildroot

%files -f %name.lang 
%defattr(0755,root,root,0755)

%py_puresitedir/SCRIBES
%_bindir/%name
%_datadir/%name/
%_datadir/pixmaps/%name.png
%_datadir/gnome/help/%name/
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/omf/%name/
%_sysconfdir/gconf/schemas/%name.schemas
%_datadir/applications/%name.desktop

%defattr(0644,root,root,0755) 
%doc AUTHORS ChangeLog CONTRIBUTORS COPYING NEWS README TRANSLATORS TODO 
