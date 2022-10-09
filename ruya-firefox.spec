Name: ruya-firefox
Version: 0.1
Release: 1%{?dist}
Summary: Ruya Firefox Settings
Summary(ar): إعدادات رؤية لفيرفكس
License: GPLv3
URL: https://ruya.parmg.sa
Requires: firefox
BuildArch: noarch

%description
Ruya Firefox Settings

%description -l ar
إعدادات رؤية لفيرفكس
%install
mkdir -p $RPM_BUILD_ROOT%{_libdir}/firefox/browser/defaults/preferences
echo 'pref("browser.startup.homepage", "data:text/plain,browser.startup.homepage=https://ruya.parmg.sa");
pref("general.autoScroll", true);
' > $RPM_BUILD_ROOT%{_libdir}/firefox/browser/defaults/preferences/firefox-ruya-default-prefs.js

%files
%{_libdir}/firefox/browser/defaults/preferences/firefox-ruya-default-prefs.js

%changelog
* Sun Oct 9 2022 Mosaab Alzoubi <mossab[AT]parmg[DOT]sa> - 0.1-1
- Initial
