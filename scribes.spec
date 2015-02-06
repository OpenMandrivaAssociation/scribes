%define name	scribes
%define version 0.3.3.3
%define release 8

%define debug_package %{nil}

Summary:	Simple yet powerful GNOME text editor
Name:		%name
Version:	%version
Release:	%release
License:	GPLv2+
Group:		Editors
URL:		http://scribes.sourceforge.net
Source0:	http://internap.dl.sourceforge.net/sourceforge/scribes/%name-%version.tar.bz2
BuildRoot:	%_tmppath/%name-%version-%release-buildroot
BuildRequires:	libxslt-proc pygtk2.0-devel yelp dbus-python gnome-python gnome-python-extras gnome-python-gtkspell gnome-python-gtksourceview desktop-file-utils
BuildRequires:	intltool
BuildRequires:  pkgconfig(gnome-doc-utils)
Requires:	yelp dbus-python pygtk2.0 gnome-python gnome-python-extras gnome-python-gtkspell
Requires:	pygtk2.0-libglade gnome-python-gtksourceview gnome-python-gconf

%description
Scribes is a text editor for GNOME that is simple, slim, and sleek, yet
powerful.

Scribes focuses on streamlining your workflow.  It does so by ensuring common
and repetitive operations are intelligently automated, and also by eliminating
factors that prevent you from focusing on your task.

%prep
%setup -q

%build
%configure2_5x --disable-scrollkeeper --disable-schemas-install
%make

%install
%makeinstall_std
desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="Utility" \
  --add-category="TextEditor" \
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
%defattr(-,root,root)
%doc AUTHORS ChangeLog CONTRIBUTORS COPYING NEWS README TRANSLATORS TODO
%py_puresitedir/SCRIBES
%_bindir/%name
%_datadir/%name/
%_datadir/pixmaps/%name.png
%_datadir/gnome/help/%name/
%_iconsdir/hicolor/*/apps/%name.*
%_datadir/omf/%name/
%_sysconfdir/gconf/schemas/%name.schemas
%_datadir/applications/%name.desktop


%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.3.3.3-6mdv2011.0
+ Revision: 677874
- fix install
- br intltool
- rebuild to add gconftool as req

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 0.3.3.3-5mdv2011.0
+ Revision: 541545
- fix perms

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 0.3.3.3-5mdv2010.0
+ Revision: 445091
- rebuild

* Tue Jan 06 2009 Funda Wang <fwang@mandriva.org> 0.3.3.3-4mdv2009.1
+ Revision: 326125
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.3.3.3-3mdv2009.0
+ Revision: 269245
- rebuild early 2009.0 package (before pixel changes)

  + Austin Acton <austin@mandriva.org>
    - tidy description

* Sun May 18 2008 Bogdano Arendartchuk <bogdano@mandriva.com> 0.3.3.3-2mdv2009.0
+ Revision: 208810
- Added missing dependencies for gconf, gtksourceview and libglade. Pointed
  out by elyezer @ #mandriva-br.

* Sun Jan 06 2008 Funda Wang <fwang@mandriva.org> 0.3.3.3-1mdv2008.1
+ Revision: 146001
- New version 0.3.3.3

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Fri Dec 28 2007 Funda Wang <fwang@mandriva.org> 0.3.3.1-1mdv2008.1
+ Revision: 138866
- New version 0.3.3.1

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 07 2007 Funda Wang <fwang@mandriva.org> 0.3.2.8-1mdv2008.0
+ Revision: 36417
- New version

* Fri May 18 2007 Adam Williamson <awilliamson@mandriva.org> 0.3.2.5-2mdv2008.0
+ Revision: 28297
- fix menu entry categories
- bump release
- buildrequires libxslt-proc

* Thu May 17 2007 Adam Williamson <awilliamson@mandriva.org> 0.3.2.5-1mdv2008.0
+ Revision: 27569
- 0.3.2.5

* Mon May 14 2007 Adam Williamson <awilliamson@mandriva.org> 0.3.2.2-1mdv2008.0
+ Revision: 26600
- Import scribes

