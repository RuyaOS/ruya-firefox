Name: ruya-firefox
Version: 0.2
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
echo 'pref("browser.startup.homepage", 'https://ruya.parmg.sa');
pref("general.autoScroll", true);
pref("browser.bookmarks.restore_default_bookmarks", true);
pref("browser.startup.firstrunSkipsHomepage", false);
pref("toolkit.telemetry.reportingpolicy.firstRun", false);
pref("browser.newtabpage.pinned",           '[{"url":"https://ruya.parmg.sa","title":"RuyaOS"}]');
pref("browser.toolbars.bookmarks.visibility", 'never');
pref("trailhead.firstrun.didSeeAboutWelcome", false);
pref("browser.aboutwelcome.enabled", false);' > $RPM_BUILD_ROOT%{_libdir}/firefox/browser/defaults/preferences/firefox-Ruya-default-prefs.js

%files
%{_libdir}/firefox/browser/defaults/preferences/firefox-Ruya-default-prefs.js

%changelog
* Sun Oct 9 2022 Mosaab Alzoubi <mossab[AT]parmg[DOT]sa> - 0.2-1
- Fixes

* Sun Oct 9 2022 Mosaab Alzoubi <mossab[AT]parmg[DOT]sa> - 0.1-1
- Initial
