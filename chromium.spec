%global chromium_path /opt/chromium-browser

Name:		chromium
Version:	52.0.2743.0
Release:	1%{?dist}
Summary:	A WebKit powered web browser

License:	BSD and LGPLv2+
Group:		Applications/Internet

Source0:	Linux_x64-394941-chrome-linux.zip

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      x86_64

%description
Chromium is an open-source web browser, powered by WebKit.
Upstream to Google Chrome.

%prep
/usr/bin/unzip -q %{SOURCE0} -d %{name}-%{version}


%install
rm -rf %{buildroot}
install -d %{buildroot}%{chromium_path}
install -d %{buildroot}%{_bindir}
cp -a %{name}-%{version}/chrome-linux/. %{buildroot}%{chromium_path}
ln -s %{chromium_path}/chrome-wrapper %{buildroot}%{_bindir}/chromium-browser
mv %{buildroot}%{chromium_path}/chrome_sandbox %{buildroot}%{chromium_path}/chrome-sandbox

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%attr(755,root,root) %{chromium_path}
%attr(4755,root,root) %{chromium_path}/chrome-sandbox
%{_bindir}/chromium-browser

%changelog
* Wed Aug 24 2016 Hung Cao Hiep <hung.cao@gooddata.com> - 52.0.2743.0
- PAAS-5602 Build new package v52.0.2743.0
